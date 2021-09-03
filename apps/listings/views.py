# apps/listings/views.py

# # Django modules
# from django.shortcuts import render

# # Locals
# from apps.listings.models import Category, Product

# # Create your views here.

# # Homepage views
# def product_list(request):
# 	categories = Category.objects.all()
# 	products = Product.objects.all()
# 	context = {
# 		'categories': categories,
# 		'products': products
# 	}
# 	return render(request,'product/list.html', context)


# ----------7.7.33.4 Filtering by category -------------------------

# apps/listings/views.py

# Django modules
from django.shortcuts import render, get_object_or_404, redirect
from apps.listings.models import Category, Product, Review  
from apps.listings.forms import ReviewForm
from apps.cart.forms import CartAddProductForm

# Views: Product list
def product_list(request, category_slug=None):

	categories = Category.objects.all()
	requested_category = None
	products = Product.objects.all()

	if category_slug:
		requested_category = get_object_or_404(Category, slug=category_slug)
		products = Product.objects.filter(category=requested_category)

	context = {
		'categories': categories,
		'requested_category': requested_category,
		'products': products	
	}	
	
	return render(request,'product/list.html', context)



# # Views: Product detail (1)
# def product_detail(request, category_slug, product_slug):
	
# 	category 	= get_object_or_404(Category, slug=category_slug)
# 	product 	= get_object_or_404(Product, category_id=category.id, slug=product_slug)
	
# 	context 	= {'product': product}
	
# 	return render(request, 'product/detail.html', context)


# Views: Product detail (2)
def product_detail(request, category_slug, product_slug):
	
	category 	= get_object_or_404(Category, slug=category_slug)
	product 	= get_object_or_404(Product, category_id=category.id, slug=product_slug)
	

	if request.method == 'POST':
		review_form = ReviewForm(request.POST)
	
		if review_form.is_valid():
			cf = review_form.cleaned_data
	
			author_name = "Anonymous"
			Review.objects.create(
				product = product,
				author = author_name,
				rating = cf['rating'],
				text = cf['text']
			)

		return redirect('listings:product_detail',
				category_slug=category_slug, product_slug=product_slug)

	else:
		review_form = ReviewForm()
		cart_product_form = CartAddProductForm()

		context 	= {
			'product': product,
			'review_form': review_form,
			'cart_product_form': cart_product_form
		}

		return render(request, 'product/detail.html', context)		

