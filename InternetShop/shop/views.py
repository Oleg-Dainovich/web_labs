from django.shortcuts import render
from cart.forms import CartAddProductForm
from django.shortcuts import render, get_object_or_404
from .models import Category, Product
import requests

def main_page(request):
    return render(request, 'shop/main.html')

def product_list(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)

    try:
        r = requests.get('https://catfact.ninja/fact?max_length=100')
        fun_fact = r.json()['fact']

    except:
        fun_fact = "Проверьте соединене..."

    return render(request, 'shop/product/list.html', {'category': category,
                                                    'categories': categories,
                                                    'products': products,
                                                    'fun_fact': fun_fact})


def product_detail(request, id, slug):
    product = get_object_or_404(Product,
                                id=id,
                                slug=slug,
                                available=True)
    cart_product_form = CartAddProductForm()
    return render(request,
                  'shop/product/detail.html',
                  {'product': product,'cart_product_form': cart_product_form})
