from django.db import models

# Create your models here.

class User(models.Model): #models.Model 을 반드시 상속받아야 함

    id = models.CharField(primary_key=True,max_length=50)
    password = models.CharField(max_length=50, null=False)
    name = models.CharField(max_length=50, null=False)
    sex = models.CharField(max_length=50, null=False)
    age = models.CharField(max_length=50, null=False)
    style_category = models.CharField(max_length=50, null=False)
    email = models.CharField(max_length=50, blank=True)