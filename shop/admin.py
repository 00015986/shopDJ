from django.contrib import admin
from .models import Category, Tag, Product


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):   # CategoryAdmin model
    list_display = ['id', 'name', 'slug']
    prepopulated_fields = {'slug': ('name',)}
    search_fields = ['name']

# Updated: 2nd Try to test the part of the code with current date.
@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):   # TagAdmin model
    list_display = ['id', 'name']
    search_fields = ['name']


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):  # ProductAdmin model 
    list_display = ['id', 'name', 'category', 'price', 'stock', 'available']
    list_filter = ['available', 'category']
    list_editable = ['price', 'stock', 'available']
    search_fields = ['name', 'description']
    prepopulated_fields = {'slug': ('name',)}
    filter_horizontal = ['tags']
    
    fieldsets = (
        ('Basic Info', {
            'fields': ('name', 'slug', 'description')
        }),
        ('Classification', {
            'fields': ('category', 'tags')
        }),
        ('Pricing & Stock', {
            'fields': ('price', 'stock', 'available')
        }),
        ('Media', {
            'fields': ('image',)
        }),
    )
