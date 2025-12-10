from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as auth_login, logout
from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required # این خط را اضافه کنید

# -------------------- ثبت نام (Sign Up) --------------------
def sign_up(request):
    if request.method == "POST":
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        username = request.POST.get("username")
        password = request.POST.get("password")
        repassword = request.POST.get("repassword")

        # بررسی مطابقت رمزها
        if password != repassword:
            messages.error(request, "رمز عبور و تکرار آن یکسان نیستند ❌")
            return render(request, "signup.html") # مسیر تمپلیت را اصلاح کردم

        # بررسی تکراری نبودن نام کاربری
        if User.objects.filter(username=username).exists():
            messages.error(request, "این نام کاربری قبلاً استفاده شده ⚠️")
            return render(request, "signup.html") # مسیر تمپلیت را اصلاح کردم

        # ایجاد کاربر جدید
        user = User.objects.create_user(
            username=username,
            password=password,
            first_name=first_name,
            last_name=last_name
        )
        user.save()
        messages.success(request, f"ثبت‌نام با موفقیت انجام شد {first_name} عزیز! 💚")
        return redirect("accunt:login")

    return render(request, "signup.html") # مسیر تمپلیت را اصلاح کردم


# -------------------- ورود (Login) --------------------
def login_view(request): # نام تابع را به login_view تغییر دادم تا با تابع built-in Django تداخل نداشته باشد
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth_login(request, user)
            messages.success(request, f"خوش اومدی {user.first_name}! 🌟")
            return redirect("home") # فرض می‌کنم 'home' در روت URLConf (amazon.urls) تعریف شده
        else:
            messages.error(request, "نام کاربری یا رمز عبور اشتباست ⚠️")
            return render(request, "login.html") # مسیر تمپلیت را اصلاح کردم

    return render(request, "login.html") # مسیر تمپلیت را اصلاح کردم


# -------------------- خروج (Logout) --------------------
def logout_user(request):
    logout(request)
    messages.info(request, "با موفقیت خارج شدی 👋")
    return redirect("accunt:login")

# -------------------- پروفایل (Profile) --------------------
@login_required # این دکوراتور تضمین می‌کند که فقط کاربران وارد شده به این صفحه دسترسی داشته باشند
def profile_view(request): # تابع جدید profile_view
    return render(request, 'profile.html', {'user': request.user})
