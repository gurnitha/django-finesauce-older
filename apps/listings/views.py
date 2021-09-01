# apps/listings/views.py

# Django modules
from django.shortcuts import render

# Locals
from apps.listings.models import Category, Product

# Create your views here.

# Homepage views
def product_list(request):
	categories = Category.objects.all()
	products = Product.objects.all()
	context = {
		'categories': categories,
		'products': products
	}
	return render(request,'product/list.html', context)