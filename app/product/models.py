from django.db import models

# Create your models here.
class Category(models.Model):
    title = models.CharField(max_length=50, unique=True, verbose_name='Category Title')
    description = models.TextField(max_length=255, null=True, blank=True, verbose_name='Description')
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.category_title

class SubCategory(models.Model):
    subcategory_title = models.CharField(max_length=50, unique=True, verbose_name='Sub-Category Title')
    subcategory_description = models.TextField(max_length=255, null=True, blank=True, verbose_name='Description')
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.subcategory_title

class Product(models.Model):
    product_name = models.CharField(max_length=255, verbose_name='Product Name')
    short_description = models.TextField(max_length=500, null=True, blank=True, verbose_name='Short Description')
    long_description = models.TextField(max_length=10000, null=True, blank=True, verbose_name='Long Description')
    category = models.ForeignKey(Category, null=True, blank=True, on_delete=models.SET_NULL)
    price = models.PositiveIntegerField(default=0, verbose_name='Price')
    is_available = models.BooleanField(default=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True, auto_now=False, editable=False)
    updated_at = models.DateTimeField(auto_now_add=False, auto_now=True, editable=False)

    def __str__(self):
        return self.product_name

