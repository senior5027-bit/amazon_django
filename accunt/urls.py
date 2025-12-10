# accunt/urls.py

from django.urls import path
from . import views

app_name = 'accunt' # این خط برای namespace ضروریه

urlpatterns = [
    path("login/", views.login_view, name="login"), # به views.login_view تغییر یافت
    path("logout/", views.logout_user, name="logout"),
    path("signup/", views.sign_up, name="signup"),
    path("profile/", views.profile_view, name="profile"), # این خط جدید اضافه شد
]
