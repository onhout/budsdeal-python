from django.forms import ModelForm
from .models import Item


class AddProductForm(ModelForm):
    class Meta:
        model = Item
        fields = ['name', 'type', 'brand', 'description', 'price', 'item_pic']

    def __init__(self, *args, **kwargs):
        super(AddProductForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'
