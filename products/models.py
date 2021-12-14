from django.db import models
from profiles.models import UserProfile
from django.db.models import Avg, Count
from decimal import Decimal

RATING_OPTIONS = [
    (Decimal(str(i*0.5)), str(i*0.5)) for i in range(11)
]


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
    class Product_status(models.TextChoices):
        LOWSTOCK = "Low Stock",
        INSTOCK = "In Stock",
        OUTOFSTOCK = "Out of Stock"

    def get_default_products_others_bought():
        default_products_others_bought = ["1", "5", "10", "15"]
        return str("_".join(default_products_others_bought))

    sku = models.CharField(max_length=254, null=True, blank=True)
    name = models.CharField(max_length=254)
    category = models.ForeignKey(
        'Category', null=True, blank=True, on_delete=models.SET_NULL)
    description = models.TextField()
    has_sizes = models.BooleanField(default=False, null=True, blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    product_rating = models.DecimalField(
        max_digits=6, decimal_places=2, null=True, default=0)
    product_type = models.CharField(max_length=254, null=True, blank=True)
    products_others_bought = models.CharField(
        max_length=254, default=get_default_products_others_bought,
        null=True, blank=True)
    status = models.CharField(
        max_length=254, choices=Product_status.choices,
        default=Product_status.INSTOCK)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name

    def getAverageRating(self):
        reviews = Review.objects.filter(product=self).aggregate(
            average=Avg('rating'))
        if reviews['average']:
            return float(reviews['average'])
        else:
            return 0

    def getNumOfReviews(self):
        reviews = Review.objects.filter(product=self).aggregate(
            numOfReviews=Count('id'))
        return reviews['numOfReviews'] if reviews['numOfReviews'] else 0


class Review(models.Model):
    product = models.ForeignKey(
        'Product', null=True, blank=True, on_delete=models.SET_NULL)
    user_profile = models.ForeignKey(
        UserProfile, on_delete=models.SET_NULL, null=True,
        blank=True, related_name='reviews')
    rating = models.DecimalField(
        max_digits=3, decimal_places=2, null=True,
        blank=True, choices=RATING_OPTIONS, default=Decimal("3.0"))
    user_review = models.TextField(max_length=200, null=False, blank=False)
    submitted_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user_profile.user.username
