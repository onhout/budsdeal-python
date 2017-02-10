from django.contrib.auth.forms import AdminPasswordChangeForm, PasswordChangeForm
from django.forms import ModelForm
from .models import Profile
from django.contrib.auth.admin import User


class PasswordChangeCustomForm(PasswordChangeForm):
    def __init__(self, user, *args, **kwargs):
        super(PasswordChangeCustomForm, self).__init__(user, *args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'


class AdminPasswordChangeCustomForm(AdminPasswordChangeForm):
    def __init__(self, user, *args, **kwargs):
        super(AdminPasswordChangeCustomForm, self).__init__(user, *args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'


class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        fields = ['gender', 'locale', 'facebook_id']

    def __init__(self, *args, **kwargs):
        super(ProfileForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'


class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name']

    def __init__(self, *args, **kwargs):
        super(UserForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'
