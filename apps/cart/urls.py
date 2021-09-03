# apps/cart/urls.py

# Django modules
from django.urls import path

# Locals
from apps.cart.views import detail_cart, add_cart, remove_cart

# Appname
app_name = 'cart'

# URLs
urlpatterns = [
	path('', detail_cart, name='detail_cart'),
	path('add/<int:product_id>/', add_cart, name='add_cart'),
	path('remove/<int:product_id>/', remove_cart, name='remove_cart'),
]