# apps/listings/urls.py

# Django modules
from django.urls import path

# Django locals
from apps.listings.views import product_list

# appname
app_name = 'listings'

urlpatterns = [
    path('', product_list, name='product_list'),
    path('<slug:category_slug>', product_list, name='product_list_by_category'),
]
