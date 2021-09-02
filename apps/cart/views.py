# apps/cart/views.py

# Django modules
from django.shortcuts import render
from django.conf import settings

# Create your views here.

def get_cart(request):
	cart = request.session.get(settings.CART_ID)
	if not cart:
		cart = request.session[settings.CART_ID] = {}
	return cart
