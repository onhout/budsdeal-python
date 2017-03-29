from django.contrib import messages
from django.contrib.auth import logout as auth_logout, update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.db.models import Sum, F, Avg, Count
from django.http import JsonResponse
from django.shortcuts import render, redirect

from apps.products.models import Item
from . import forms as user_forms
from .models import Profile


# Create your views here.


def signup(request):
    return render(request, 'registration/signup.html')


def login(request):
    if request.user.is_authenticated and not request.user.is_anonymous:
        return redirect('/user/home')
    else:
        return render(request, 'registration/login.html')


def logout(request):
    auth_logout(request)
    return redirect('/user/login')


def view_profile(request, display_name):
    user_profile = Profile.objects.get(display_name=display_name)
    this_user = User.objects.get(id=user_profile.user_id)
    if this_user.id == request.user.id:
        return redirect('/user/home')
    else:
        return render(request, 'profiles/view_profile.html', {
            'this_user': this_user
        })


@login_required(login_url='/user/login')
def home(request):
    user_products = Item.objects.filter(user=request.user)
    products_count = user_products.count()
    products_extra_info = user_products.aggregate(Sum('view_count'), total=Sum(F('price') * F('count')))
    return render(request, 'profiles/user_home.html', {
        'products_count': products_count,
        'products_extra_info': products_extra_info
    })


@login_required
def account_settings_password(request):
    if request.user.has_usable_password():
        password_form = user_forms.PasswordChangeCustomForm
    else:
        password_form = user_forms.AdminPasswordChangeCustomForm

    if request.POST:
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
    return render(request, 'profiles/settings/password.html', {'form': form})


@login_required
def user_profile(request):
    user_form = user_forms.UserForm(instance=request.user)
    profile_form = user_forms.ProfileForm(instance=request.user.profile)

    return render(request, 'profiles/settings/user_profile.html', {
        'user_form': user_form,
        'profile_form': profile_form
    })


@login_required
def user_company(request):
    profile = request.user.profile
    if profile.approved_as_seller:
        company_form = user_forms.CompanyForm(instance=request.user.company)
        return render(request, 'profiles/settings/user_company.html', {
            'company_form': company_form
        })
    else:
        return render(request, 'profiles/user_home.html', {
        })


@login_required
def save_account_settings(request):
    if request.POST:
        user_form = user_forms.UserForm(request.POST, instance=request.user)
        profile_form = user_forms.ProfileForm(request.POST, instance=request.user.profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            return redirect('user_home')


@login_required
def save_company_info(request):
    profile = request.user.profile
    if request.POST and profile.approved_as_seller:
        company_form = user_forms.CompanyForm(request.POST, instance=request.user.company)
        company_form.save()
        return redirect('user_home')


@login_required
def register_as_seller(request):
    profile = request.user.profile
    if request.user.is_authenticated and not profile.approved_as_seller:
        return render(request, 'profiles/register_as_seller.html')
    else:
        return redirect('user_home')


@login_required
def user_feedback(request, display_name):
    userProfile = Profile.objects.get(display_name=display_name)
    user = User.objects.get(id=userProfile.user_id)
    if request.POST and request.user.is_authenticated:
        feedbackForm = user_forms.FeedBackForm(request.POST)
        feedbackForm.save(commit=False)
        feedbackForm.from_user = request.user
        feedbackForm.to_user = user
        feedbackForm.save()
        data = {
            'rating': user.feedback_to_user.aggregate(avg=Avg('user_rating'), count=Count('user_rating'))
        }
    else:
        data = {
            'rating': user.feedback_to_user.aggregate(avg=Avg('user_rating'), count=Count('user_rating'))
        }
    return JsonResponse(data)
