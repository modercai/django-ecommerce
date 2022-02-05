from django.shortcuts import render, get_object_or_404
from .models import Product, Category

# Create your views here.


def categories(request):
    return{
        'categories': Category.objects.all()
    }


def homePage(request):
    products = Product.products.all()
    return render(request, 'shop/home.html', {'products': products})


def product_detail(request, slug):
    product = get_object_or_404(Product, slug=slug, in_stock=True)
    return render(request, 'shop/products/product_detail.html', {'product': product})


def category_list(request, category_slug):
    category = get_object_or_404(Category, slug=category_slug)
    products = Product.objects.filter(category=category)
    return render(request,  'shop/products/category.html', {'category': category, 'products': products})
