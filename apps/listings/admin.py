# apps/listings/admin.py

# Django modules
from django.contrib import admin

# Django locals
from apps.listings.models import Category, Product, Review

# Register your models here.
admin.site.register(Review)
class OrderReviewInline(admin.TabularInline):
	model = Review


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
	list_display = ('name', 'slug')
	prepopulated_fields = {'slug': ('name',)}


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
	list_display =('name', 'category', 'slug', 'price', 'available')
	list_filter = ('category', 'available')
	list_editable = ('price', 'available')
	prepopulated_fields = {'slug': ('name',)}	

	# inlines = [OrderReviewInline]


