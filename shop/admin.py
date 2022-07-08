from django.contrib import admin
from .models import Category, Product


# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(Category, CategoryAdmin)


class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'stock', 'availability', 'created_on', 'updated_on']
    prepopulated_fields = {'slug': ('name',)}
    list_editable = ['price', 'stock', 'availability']


admin.site.register(Product, ProductAdmin)
