# E:/tamrin_kelas/core/urls.py

from django.urls import path
from . import views

app_name = 'core' # حتماً این خط را اضافه کنید

urlpatterns = [
    path('', views.home, name='home'),
    path('test/', views.test_page, name='test_page'), # الگوی URL برای test_page
    path('contact-us/', views.contact_us, name='contact_us'), # الگوی URL برای تماس با ما
]
