from django import forms
from django.forms import ModelForm

from . import models


class OrderForm(ModelForm):
    class Meta:
        model = models.Order
        exclude = ['buyer', 'item', 'order_status', 'timestamp', 'editable']
        widgets = {
            'additional_info': forms.Textarea(
                attrs={'placeholder': 'Additional terms and conditions'}
            )
        }

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        super(OrderForm, self).__init__(*args, **kwargs)
        try:
            instance = getattr(self, 'instance', None)
            if instance.order_status == 'canceled' or instance.order_status == 'confirmed' or instance.editable != self.user:
                for field in self.fields:
                    self.fields[field].widget.attrs['disabled'] = True
        except:
            pass

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
