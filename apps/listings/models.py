# apps/listings/models.py

# Django modules
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.

# MODEL:Category
class Category(models.Model):

	name = models.CharField(max_length=100,unique=True)
	slug = models.SlugField(max_length=100,unique=True)

	class Meta:
		ordering = ('-name',)
		verbose_name_plural = 'categories'

	def __str__(self):
		return self.name


# MODEL:Product
class Product(models.Model):

	category = models.ForeignKey(Category,related_name='products',on_delete = models.CASCADE)
	name = models.CharField(max_length=100,unique=True)
	slug = models.SlugField(max_length=100,unique=True)
	image = models.ImageField(upload_to='products/')
	description = models.TextField()
	shu = models.CharField(max_length=10)
	price = models.DecimalField(max_digits=10,decimal_places=2)
	available = models.BooleanField(default=True)

	class Meta:
		ordering = ('shu',)


class Review(models.Model):
	product = models.ForeignKey(
		Product,
		related_name='reviews',
		on_delete=models.CASCADE
	)
	author = models.CharField(max_length=50)
	rating = models.IntegerField(
		validators=[MinValueValidator(1), MaxValueValidator(5)]
	)
	text = models.TextField(blank=True)
	created = models.DateTimeField(auto_now_add=True)

	class Meta:
		ordering = ('-created',)


