from django.urls import path
from . import views

app_name = 'product' # این خط رو اضافه کن تا بتونیم در تمپلیت‌ها از نامگذاری معکوس (reverse naming) استفاده کنیم

urlpatterns = [
    path('', views.product_list, name='product_list'),
    path('<int:id>/', views.product_detail, name='product_detail'),
]
