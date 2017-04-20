# In consumers.py
import json

from channels import Group
from channels.auth import channel_session_user, channel_session_user_from_http

from .models import Order, Messages


# Connected to websocket.connect
@channel_session_user_from_http
def ws_connect(message):
    # Accept connection
    message.reply_channel.send({"accept": True})
    # Add them to the right group
    room = message.content['query_string'][9:]
    # Save room in session and add us to the group
    message.channel_session['order_id'] = room

    order = Order.objects.get(pk=message.channel_session['order_id'])
    # message.channel_session['current_order'] = order
    if order.buyer == message.user or order.item.user == message.user:
        Group("order-%s" % room).add(message.reply_channel)


# Connected to websocket.receive
@channel_session_user
def ws_message(message):
    Group("order-%s" % message.channel_session['order_id']).send({
        "text": json.dumps({
            "display_name": message.user.profile.display_name,
            "profile_pic": '/%s' % message.user.profile.profile_photo,
            "full_name": message.user.get_full_name(),
            "msg": message['text']
        })
    })
    save_message = Messages.objects.create(order_id=message.channel_session['order_id'],
                                           sender_id=message.user.id)
    save_message.content = message['text']
    save_message.save()


# Connected to websocket.disconnect
@channel_session_user
def ws_disconnect(message):
    Group("order-%s" % message.channel_session['order_id']).discard(message.reply_channel)
