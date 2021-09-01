# apps/listings/views.py

# Django modules
from django.shortcuts import render

# Locals
from apps.listings import Category, Product

# Create your views here.

# Homepage views
def product_list(request):
	categories = Category.objects.all()
	products = Product.objects.all()
	context = {
		'categories': categories,
		'products': products
	}
	return render(equest,'product/list.html', context)