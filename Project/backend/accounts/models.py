from django.db import models

# Create your models here.
class User(models.Model):
    phoneNum = models.CharField(max_length=20)
    point = models.IntegerField()

class Coupon(models.Model):
    code = models.CharField(max_length=12)
    user = models.ForeignKey('User', on_delete=models.CASCADE)

class Class5(models.Model):
    user = models.ForeignKey('User', on_delete=models.CASCADE)
    letter = models.TextField()