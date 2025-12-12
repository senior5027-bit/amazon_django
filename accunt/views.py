from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import SignupForm


def sign_up(request):
    form = SignupForm()

    if request.method == "POST":
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "ثبت نام با موفقیت انجام شد")
            return redirect("accunt:login")

    return render(request, "signup.html", {"form": form})


def login(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)
        if user:
            auth_login(request, user)
            return redirect("core:home")
        else:
            messages.error(request, "نام کاربری یا رمز عبور اشتباه است")

    return render(request, "login.html")


def logout_user(request):
    logout(request)
    return redirect("accunt:login")


@login_required
def profile_view(request):
    return render(request, "profile.html")
