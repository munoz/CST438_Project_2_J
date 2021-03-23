from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class WishList(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="wishlist", null=True)
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Task(models.Model):
    wishlist = models.ForeignKey(WishList, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    complete = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class displayusername(models.Model):
    username = models.CharField(max_length=100)