from django.urls import path
from . import views

app_name = 'shop'

# URL patterns for the shop app
urlpatterns = [
    path('', views.product_list, name='product_list'),
    path('category/<slug:category_slug>/', views.product_list, name='product_list_by_category'),
    path('product/<int:pk>/<slug:slug>/', views.product_detail, name='product_detail'),
    path('categories/', views.category_list, name='category_list'),
    path('category/create/', views.category_create, name='category_create'),
]
