from django.forms import ModelForm
from django.forms.widgets import CheckboxSelectMultiple
from .models import Item, Category


class AddProductForm(ModelForm):
    class Meta:
        model = Item
        exclude = 'id', 'user'

    def __init__(self, *args, **kwargs):
        super(AddProductForm, self).__init__(*args, **kwargs)
        # self.fields['categories'].widget = CheckboxSelectMultiple()
        self.fields['categories'].queryset = Category.objects.filter(parent_category__isnull=False)
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'
            if self.fields[field].required:
                self.fields[field].help_text = '*required'


class EditProductForm(ModelForm):
    class Meta:
        model = Item
        exclude = 'id', 'user'

    def __init__(self, *args, **kwargs):
        super(EditProductForm, self).__init__(*args, **kwargs)
        self.fields['categories'].queryset = Category.objects.filter(parent_category__isnull=False)
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'
            if self.fields[field].required:
                self.fields[field].help_text = '*required'
