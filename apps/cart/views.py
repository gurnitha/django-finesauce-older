# apps/cart/views.py

# Django modules
from django.shortcuts import render, redirect, get_object_or_404
from django.conf import settings
from decimal import Decimal

# Locals
from listings.models import Product
from apps.cart.forms import CartAddProductForm

# Create your views here.

def get_cart(request):
	cart = request.session.get(settings.CART_ID)
	if not cart:
		cart = request.session[settings.CART_ID] = {}
	return cart


def add_cart(request, product_id):
	cart = get_cart(request)
	product = get_object_or_404(Product, id=product_id)
	product_id = str(product.id)
	form = CartAddProductForm(request.POST)

	if form.is_valid():
		cd = form.cleaned_data

		if product_id not in cart:
			cart[product_id] = {
				'quantity': 0,
				'price': str(product.price)
		}

	if request.POST.get('overwrite_qty'):
		cart[product_id]['quantity'] = cd['quantity']
	
	else:
		cart[product_id]['quantity'] += cd['quantity']
	
	request.session.modified = True
	
	return redirect('cart:cart_detail')
