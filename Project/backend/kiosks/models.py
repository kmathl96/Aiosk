from django.db import models
from accounts.models import User
from django.db.models.signals import post_delete
from django.dispatch import receiver

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=10)

class Menu(models.Model):
    name = models.CharField(max_length=20)
    price = models.IntegerField()
    description = models.CharField(max_length=300)
    image_path = models.CharField(max_length=50)
    category = models.ForeignKey('Category', on_delete=models.CASCADE)

class VirtualUser(models.Model):
    age = models.CharField(max_length=10)

class Order(models.Model):
    virtual_user = models.ForeignKey('VirtualUser', on_delete=models.SET_DEFAULT, default=0)
    date = models.DateTimeField(auto_now=True)
    price = models.IntegerField()

class Detail(models.Model):
    menu = models.ForeignKey('Menu', on_delete=models.SET_DEFAULT, default=0)
    amount = models.IntegerField()
    # size = models.CharField(max_length=10)
    # temperature = models.BooleanField()
    order = models.ForeignKey('Order', on_delete=models.CASCADE)

class Season(models.Model):
    name = models.CharField(max_length=10)

class VirtualHistory(models.Model):
    user = models.ForeignKey(VirtualUser, on_delete=models.CASCADE)
    menu = models.ForeignKey('Menu', on_delete=models.CASCADE)
    season = models.ForeignKey('Season', on_delete=models.CASCADE)
    count = models.IntegerField(default=0)

class History(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    menu = models.ForeignKey('Menu', on_delete=models.CASCADE)
    season = models.ForeignKey('Season', on_delete=models.CASCADE)
    count = models.IntegerField(default=0)
    updated_at = models.DateTimeField(auto_now_add=True)

class Detection(models.Model):
    images = models.ImageField(blank=True, upload_to="images", null=True)

@receiver(post_delete, sender=Detection)
def submission_delete(sender, instance, **kwargs):
    instance.images.delete(False)

class Recommend(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE)