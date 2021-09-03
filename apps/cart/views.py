# apps/cart/views.py

# Django modules
from django.shortcuts import render, redirect, get_object_or_404
from django.conf import settings
from decimal import Decimal

# Locals
from listings.models import Product
from apps.cart.forms import CartAddProductForm

# Create your views here.

# View:get_cart
def get_cart(request):
	cart = request.session.get(settings.CART_ID)
	if not cart:
		cart = request.session[settings.CART_ID] = {}
	return cart


# View:add_cart
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
	
	return redirect('cart:detail_cart')


# View:detail_cart
def detail_cart(request):
	cart = get_cart(request)
	product_ids = cart.keys()
	products = Product.objects.filter(id__in=product_ids)
	temp_cart = cart.copy()

	for product in products:
		cart_item = temp_cart[str(product.id)]
		cart_item['product'] = product
		cart_item['total_price'] = (Decimal(cart_item['price'])
				* cart_item['quantity'])
	
	cart_total_price = sum(Decimal(item['price']) * item['quantity']
				for item in temp_cart.values())
		
	context = {
		'cart': temp_cart.values(),
		'cart_total_price': cart_total_price	
	}

	return render(request,'detail.html', context)
