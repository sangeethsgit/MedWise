from django.db import models

class login_info(models.Model):
    Username=models.CharField(max_length=50)
    Password=models.CharField(max_length=20)
# Create your models here.

