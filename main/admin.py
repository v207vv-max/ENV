from django.contrib import admin
from .models import Product , Size ,ProductSize ,ProductImage ,Category
# Register your models here.



class ProductImageInline(admin.TabularInline):
    model = ProductImage
    extra = 1


class ProductSizeInline(admin.TabularInline):
    model = ProductSize
    extra = 1


class ProductAdmin(admin.ModelAdmin):
    list_display = ['name','category','color','price']
    list_filter = ['category','color']
    search_fields = ['name','color','description']
    populate_fields = {'slug':('name',)}
    inlines = [ProductSizeInline, ProductImageInline]


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name','slug']
    populate_fields = {'slug': ('name',)}


class SizeAdmin(admin.ModelAdmin):
    list_display = ['name']


admin.site.register(Product,ProductAdmin)
admin.site.register(Category,CategoryAdmin)
admin.site.register(Size,SizeAdmin)