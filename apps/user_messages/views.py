from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from . import models, forms
from apps.user.models import Profile
from django.contrib.auth.admin import User
from apps.products.models import Item

# Create your views here.


def view_sent_messages(request):
    messages = models.Conversations.objects.filter(from_user_id=request.user.id)
    return render(request, 'view_messages.html', {
        'inbox_type': 'Sent',
        'user_messages': messages
    })


def view_inbox_messages(request):
    messages = models.Conversations.objects.filter(to_user_id=request.user.id)
    return render(request, 'view_messages.html', {
        'inbox_type': 'Inbox',
        'user_messages': messages
    })


def send_message(request, social_id, item_id):
    user_profile = Profile.objects.get(social_id=social_id)
    this_user = User.objects.get(id=user_profile.user_id)
    regard_item = Item.objects.get(id=item_id)
    if request.POST and request.user.is_authenticated:
        message_form = forms.MessageForm(request.POST)
        if message_form.is_valid():
            form = message_form.save(commit=False)
            form.from_user_id = request.user
            form.to_user_id = this_user
            form.regard_item = regard_item
            form.save()
            return redirect('view_sent_messages')
    else:
        message_form = forms.MessageForm()

    return render(request, 'send_message.html', {
        'this_product': regard_item,
        'this_user': this_user,
        'message_form': message_form
    })


def message_details(request, message_id):
    message = models.Conversations.objects.get(id=message_id)
    return render(request, 'message_details.html', {
        'message': message
    })


def delete_message(request, message_id):
    message = models.Conversations.objects.get(id=message_id).delete()
    if request.POST and request.user.is_authenticated:
        message.save()

    return redirect('view_sent_messages')
