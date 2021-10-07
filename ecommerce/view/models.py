from django.db import models
from django.utils import timezone
from django.core.validators import MinValueValidator, MaxValueValidator
from django.urls import reverse



# Create your models here.
class Product(models.Model):
    id=models.AutoField(primary_key=True)
    name = models.CharField(max_length=20)
    brand = models.CharField(max_length=20,default=None )
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    created = models.DateTimeField(default=timezone.now)
    updated = models.DateTimeField(default=timezone.now)
    rating = models.IntegerField(default=5,validators=[MinValueValidator(0),MaxValueValidator(5)])
    image = models.ImageField(upload_to='product_pictures',default=None, null=True, blank=True)


    def __str__(self):
        return self.name


    def get_absolute_url(self):
        return reverse('ecommerce-product', kwargs={'pk' : self.pk})
