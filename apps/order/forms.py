from django import forms
from django.forms import ModelForm

from apps.user.models import Shipping
from . import models


class OrderForm(ModelForm):
    prefix = 'order_form'

    class Meta:
        model = models.Order
        exclude = ['buyer', 'seller', 'order_status', 'timestamp', 'editable']
        widgets = {
            'additional_info': forms.Textarea(
                attrs={'placeholder': 'Additional terms and conditions'}
            )
        }

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        super(OrderForm, self).__init__(*args, **kwargs)
        self.fields['shipping_address'].queryset = Shipping.objects.filter(user=self.user)
        try:
            instance = getattr(self, 'instance', None)
            if instance.order_status == 'canceled' or instance.order_status == 'confirmed' or instance.editable != self.user:
                for field in self.fields:
                    self.fields[field].widget.attrs['disabled'] = True
            if instance.buyer != self.user:
                self.fields['shipping_address'].widget.attrs['disabled'] = True

        except:
            pass

        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'


class OrderItemsForm(ModelForm):
    prefix = 'order_items_form'

    class Meta:
        model = models.OrderItems
        fields = ['item_amount']

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        super(OrderItemsForm, self).__init__(*args, **kwargs)
        try:
            instance = getattr(self, 'instance', None)
            theOrder = models.Order.objects.get(instance.order_id)
            if theOrder.order_status == 'canceled' or theOrder.order_status == 'confirmed' or theOrder.editable != self.user:
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
