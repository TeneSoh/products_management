from django.db import models
from users.models import User

# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=255, unique=True, blank=False, null=False)
    description = models.TextField(blank=False, null=False)
    # user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='products')
    price = models.DecimalField(max_digits=10, decimal_places=2)
