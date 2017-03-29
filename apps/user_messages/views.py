from django.contrib.auth.admin import User
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from apps.products.models import Item
from apps.user.models import Profile
from . import models, forms


# Create your views here.


@login_required
def view_sent_messages(request):
    messages = request.user.message_from_user.all()
    return render(request, 'user/view_messages.html', {
        'inbox_type': 'Sent',
        'user_messages': messages
    })


@login_required
def view_inbox_messages(request):
    messages = request.user.message_to_user.all()
    return render(request, 'user/view_messages.html', {
        'inbox_type': 'Inbox',
        'user_messages': messages
    })


@login_required
def send_message(request, social_id, item_id):
    user_profile = Profile.objects.get(social_id=social_id)
    this_user = User.objects.get(id=user_profile.user_id)
    regard_item = Item.objects.get(id=item_id)
    if request.POST and request.user.is_authenticated:
        message_form = forms.MessageForm(request.POST)
        if message_form.is_valid():
            form = message_form.save(commit=False)
            form.from_user = request.user
            form.to_user = this_user
            form.regard_item = regard_item
            form.save()
            return redirect('view_sent_messages')
    else:
        message_form = forms.MessageForm(initial={'subject': 'Quote regarding: ' + regard_item.name})

    return render(request, 'user/send_message.html', {
        'this_product': regard_item,
        'this_user': this_user,
        'message_form': message_form
    })


@login_required
def message_details(request, message_id):
    message = models.Conversations.objects.get(id=message_id)
    if message.to_user == request.user:
        message.read = True
        message.save()
    return render(request, 'user/message_details.html', {
        'message': message
    })


@login_required
def delete_message(request, message_id):
    message = models.Conversations.objects.get(id=message_id).delete()
    if request.POST and request.user.is_authenticated:
        message.save()

    return redirect('view_sent_messages')
