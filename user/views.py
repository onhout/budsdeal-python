from django.contrib import messages
from django.contrib.auth import logout as auth_logout
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from . import forms


# Create your views here.


def signup(request):
    return render(request, 'signup.html')


def login(request):
    if request.user.is_authenticated and not request.user.is_anonymous:
        return redirect('/user/home')
    else:
        return render(request, 'registration/login.html')


def logout(request):
    auth_logout(request)
    return redirect('/user/login')


@login_required(login_url='/user/login')
def home(request):
    return render(request, 'home.html')


@login_required
def account_settings_password(request):
    if request.user.has_usable_password():
        password_form = forms.PasswordChangeCustomForm
    else:
        password_form = forms.AdminPasswordChangeCustomForm

    if request.method == 'POST':
        form = password_form(request.user, request.POST)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            messages.success(request, 'Your password was successfully updated!')
            return redirect('password')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = password_form(request.user)
    return render(request, 'profiles/password.html', {'form': form})


@login_required
def account_settings(request):
    profile = request.user.profile
    if request.method == 'POST':
        user_form = forms.UserForm(request.POST, instance=request.user)
        profile_form = forms.ProfileForm(request.POST, instance=request.user.profile)
        company_form = forms.CompanyForm(request.POST, instance=request.user.company)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            company_form.save()
            # messages.success(request, _('Your profile was successfully updated!'))
            return redirect('user_settings')
        # else:
            # messages.error(request, _('Please correct the error below.'))
    else:
        user_form = forms.UserForm(instance=request.user)
        profile_form = forms.ProfileForm(instance=request.user.profile)

    if profile.approved_as_seller:
        company_form = forms.CompanyForm(instance=request.user.company)
        return render(request, 'profiles/settings.html', {
            'user_form': user_form,
            'profile_form': profile_form,
            'company_form': company_form
        })
    else:
        return render(request, 'profiles/settings.html', {
            'user_form': user_form,
            'profile_form': profile_form
        })
