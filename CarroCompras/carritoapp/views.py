from django.shortcuts import render, get_object_or_404, redirect
from .models import Product, CartItem
from .forms import AddToCartForm

def product_list(request):
    products = Product.objects.all()
    return render(request, 'cart/product_list.html', {'products': products})

def add_to_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    form = AddToCartForm(request.POST or None)

    if request.method == 'POST' and form.is_valid():
        cart_item, created = CartItem.objects.get_or_create(product=product)
        cart_item.quantity += form.cleaned_data['quantity']
        cart_item.save()
        return redirect('view_cart')

    return render(request, 'cart/add_to_cart.html', {'product': product, 'form': form})

def view_cart(request):
    cart_items = CartItem.objects.all()
    return render(request, 'cart/view_cart.html', {'cart_items': cart_items})

