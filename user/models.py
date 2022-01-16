from django.db import models
from django.conf import settings
# from django.contrib.auth.models import AbstractUser

User = settings.AUTH_USER_MODEL

# Create your models here.
class User(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,null=False)
    name = models.CharField(max_length=100,null=False)
    phone = models.CharField(max_length=100,null=False)
    address = models.CharField(max_length=100,null=False)
    city = models.CharField(max_length=100,null=False)
    state = models.CharField(max_length=100,null=False)
    zipcode = models.CharField(max_length=100,null=False)
    country = models.CharField(max_length=100,null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Order(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,null=False)
    symbol = models.CharField(max_length=100,null=False)
    order_type = models.CharField(max_length=100,null=False)
    time_in_force = models.CharField(max_length=100,null=False, default='day')
    type = models.CharField(max_length=100,null=False, default='market')
    quantity = models.IntegerField(null=False)
    price = models.FloatField(null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # symbol=symb,
    # qty=1,
    # side='buy',
    # type='market',
    # time_in_force='gtc'