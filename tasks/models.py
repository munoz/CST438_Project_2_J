from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class WishList(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="wishlist", null=True)
    name = models.CharField(max_length=200 )

    class Meta:
        verbose_name = "wishlist"
    def __str__(self):
        return self.name

class Task(models.Model):
    wishlist = models.ForeignKey('tasks.WishList', on_delete=models.CASCADE,verbose_name="wishlist")
    title = models.CharField(max_length=200, null=False, blank=False)
    complete = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title

class displayusername(models.Model):
    username = models.CharField(max_length=100)