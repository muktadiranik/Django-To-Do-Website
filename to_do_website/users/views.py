from django.shortcuts import render, redirect
from .forms import RegisterUserForm, AdditionalUserInfoForm
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from .models import AdditionalUserInfo
from django.contrib.auth.models import User


def update_user_profile(request, user_name):
    user_info = User.objects.get(username=user_name)
    additional_user_info = AdditionalUserInfo.objects.get(pk=user_info.id)
    form = RegisterUserForm(request.POST or None, instance=user_info)
    additional_form = AdditionalUserInfoForm(request.POST or None, request.FILES or None, instance=additional_user_info)
    if form.is_valid():
        form.save()
        if additional_form.is_valid():
            additional_form.save()
            username = request.POST['username']
            password = request.POST['password1']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, "Profile Updated!!!")
                return redirect("user_profile")

    return render(request, "update_user_profile.html", {
        "form": form,
        "additional_form": additional_form,
    })


def register_user(request):
    if request.method == "POST":
        form = RegisterUserForm(request.POST)
        additional_form = AdditionalUserInfoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            username = request.POST['username']
            password = request.POST['password1']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                if additional_form.is_valid():
                    additional_info = additional_form.save(commit=False)
                    additional_info.user = user
                    additional_info.save()
                    login(request, user)
                    return redirect("home")
    else:
        form = RegisterUserForm()
        additional_form = AdditionalUserInfoForm()
    return render(request, "register_user.html", {
        "form": form,
        "additional_form": additional_form,
    })


def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("my_to_do_list")

        else:
            messages.success(request, "Login Failed!!!")
            return render(request, "login_user.html", {})
    else:
        return render(request, "login_user.html", {})


def logout_user(request):
    logout(request)
    messages.success(request, "Logged Out!!!")
    return redirect("home")


def user_profile(request):
    user_info = AdditionalUserInfo.objects.get(pk=request.user.id)

    return render(request, "user_profile.html", {
        "user_info": user_info,
    })
