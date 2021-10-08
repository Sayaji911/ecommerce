from django.db import models
from django.utils import timezone
from django.core.validators import MinValueValidator, MaxValueValidator
from django.urls import reverse



# Create your models here.
class Product(models.Model):
    id=models.AutoField(primary_key=True) #product id
    name = models.CharField(max_length=20) # product name
    brand = models.CharField(max_length=20,default=None ) # product brand
    description = models.TextField(blank=True) # product description
    price = models.DecimalField(max_digits=10, decimal_places=2) #price
    created = models.DateTimeField(default=timezone.now)# created date
    updated = models.DateTimeField(default=timezone.now) #updted value currenty not included in views.
    #setting product rating brtween 1 and 5. if no input than 5
    rating = models.IntegerField(default=5,validators=[MinValueValidator(0),MaxValueValidator(5)])
    #image object to upload images. setting the upload folder, default will be empty, null and blank are allowed
    image = models.ImageField(upload_to='product_pictures',default=None, null=True, blank=True)


    def __str__(self): # dunder to function to return product name for use in shell
        return self.name


    def get_absolute_url(self):
        return reverse('ecommerce-product', kwargs={'pk' : self.pk})
