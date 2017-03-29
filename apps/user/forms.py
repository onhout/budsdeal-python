from django.contrib.auth.admin import User
from django.contrib.auth.forms import AdminPasswordChangeForm, PasswordChangeForm
from django.forms import ModelForm

from .models import Profile, Company, Feedback


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
        fields = ['gender']

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


class CompanyForm(ModelForm):
    class Meta:
        model = Company
        fields = ['name', 'address', 'address2', 'city', 'state', 'zip', 'phone_number', 'TIN']

    def __init__(self, *args, **kwargs):
        super(CompanyForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'
            self.fields[field].label = 'Company ' + self.fields[field].label
            if self.fields[field].required:
                self.fields[field].help_text = '*required'


class FeedBackForm(ModelForm):
    class Meta:
        model = Feedback
        exclude = ['to_user', 'from_user']