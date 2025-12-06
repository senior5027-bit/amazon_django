# cart/urls.py
from django.urls import path
from . import views # فقط این خط رو نگه دار!

app_name = 'cart' # مطمئن شو که این خط هم هست

urlpatterns = [
    path('add/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    path('remove/<int:product_id>/', views.remove_from_cart, name='remove_from_cart'),
    path('', views.cart_detail, name='cart_detail'),
    path('checkout/', views.checkout, name='checkout'),
]
