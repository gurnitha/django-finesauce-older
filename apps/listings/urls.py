# apps/listings/urls.py

# Django modules
from django.urls import path

# Django locals
from apps.listings.views import home_page

# appname
app_name = 'listings'

urlpatterns = [
    path('', home_page, name='home_page'),
]
