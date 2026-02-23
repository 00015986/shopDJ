from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Product, Category, Tag
from .forms import CategoryForm


def product_list(request, category_slug=None):
    """View all products, optionally filtered by category"""
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)
    current_category = None
    
    if category_slug:
        current_category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=current_category)
    
    context = {
        'categories': categories,
        'products': products,
        'current_category': current_category,
    }
    return render(request, 'shop/product_list.html', context)


def product_detail(request, pk, slug):
    """View one product"""
    product = get_object_or_404(Product, pk=pk, slug=slug, available=True)
    return render(request, 'shop/product_detail.html', {'product': product})


@login_required
def category_create(request):
    """Create a new category with login required"""
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Category created successfully!')
            return redirect('shop:category_list')
    else:
        form = CategoryForm()
    return render(request, 'shop/category_form.html', {'form': form, 'action': 'Create'})


def category_list(request):
    """View all different categories"""
    categories = Category.objects.all()
    return render(request, 'shop/category_list.html', {'categories': categories})
