from django.forms import ModelForm

from . import models


class OrderForm(ModelForm):
    class Meta:
        model = models.Order
        exclude = ['buyer', 'item', 'order_status', 'timestamp']

    def __init__(self, *args, **kwargs):
        super(OrderForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'


class MessageForm(ModelForm):
    class Meta:
        model = models.Messages
        exclude = ['sender', 'timestamp']

    def __init__(self, *args, **kwargs):
        super(MessageForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'
