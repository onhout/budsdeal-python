from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from . import models, forms
from apps.user.models import Profile
from django.contrib.auth.admin import User

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


def send_message(request, social_id):
    user_profile = Profile.objects.get(social_id=social_id)
    this_user = User.objects.get(id=user_profile.user_id)
    if request.POST and request.user.is_authenticated:
        message_form = forms.MessageForm(request.POST)
        if message_form.is_valid():
            form = message_form.save(commit=False)
            form.from_user_id = request.user
            form.to_user_id = this_user
            form.save()
            return redirect('view_sent_messages')
    else:
        message_form = forms.MessageForm()

    return render(request, 'send_message.html', {
        'this_user': this_user,
        'message_form': message_form
    })


