from django import forms
from django.forms import ModelForm

from . import models


class OrderForm(ModelForm):
    class Meta:
        model = models.Order
        exclude = ['buyer', 'item', 'order_status', 'timestamp']
        widgets = {
            'additional_info': forms.Textarea(
                attrs={'placeholder': 'Additional terms and conditions'}
            )
        }

    def __init__(self, *args, **kwargs):
        super(OrderForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'


class MessageForm(ModelForm):
    class Meta:
        model = models.Messages
        exclude = ['sender', 'timestamp', 'order', 'read']
        widgets = {
            'content': forms.Textarea(
                attrs={'placeholder': 'Type your replies here...', 'rows': 3}
            )
        }

    def __init__(self, *args, **kwargs):
        super(MessageForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'
