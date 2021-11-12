from django.db import models


class Category(models.Model):

    class Meta:
        verbose_name_plural = 'Categories'

    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class Product(models.Model):

    class ProductStatus(models.TextChoices):
        INSTOCK = 'In Stock'
        LOWSTOCK = 'Low on Stock'
        OUTOFSTOCK = 'Out on Stock'

    name = models.CharField(max_length=254)
    category = models.ForeignKey('Category', null=True, blank=True, on_delete=models.SET_NULL)
    sku = models.CharField(max_length=254, null=True, blank=True)
    description = models.TextField()
    has_sizes = models.BooleanField(default=False, null=True, blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    product_rating = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    product_type = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    status = models.CharField(max_length=2, choices=ProductStatus.choices, default=ProductStatus.INSTOCK)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name