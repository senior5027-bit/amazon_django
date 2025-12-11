# accunt/urls.py

from django.urls import path
from . import views

app_name = 'accunt' 

urlpatterns = [
    path("login/", views.login_view, name="login"), 
    path("logout/", views.logout_user, name="logout"),
    path("signup/", views.sign_up, name="signup"),
    path("profile/", views.profile_view, name="profile"),
]
