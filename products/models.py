from django.db import models
from users.models import User

# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=255, unique=True, blank=False, null=False)
    description = models.TextField(blank=False, null=False)
    image = models.ImageField(upload_to='products/', null=True, blank=True) # https//localhost/media/products/asasdasd.jpg
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='products')
    price = models.DecimalField(max_digits=10, decimal_places=2)
