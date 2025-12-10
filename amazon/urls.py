from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from  core.views import test_page


urlpatterns = [
    path('admin/', admin.site.urls),

    # صفحه اصلی
    path('', include('product.urls')),

    # مسیرهای اپ لاگین / ثبت‌نام
    path('accunt/', include('accunt.urls')),
    path('core/',include('core.urls')),
    path('test/',test_page,name='test_page'),
    path('cart/',include('cart.urls'))
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
