from django.contrib import admin
from .models import Product, ProductImage


class ProductImageInline(admin.TabularInline):
    model = ProductImage
    fields = ['image']
    extra = 4   # چهار فرم آپلود عکس


class ProductAdmin(admin.ModelAdmin):
    list_display = ['title', 'price']
    inlines = [ProductImageInline]


admin.site.register(Product, ProductAdmin)
