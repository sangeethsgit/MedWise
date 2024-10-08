from django.db import models

class LoginInfo(models.Model):
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=128)

class SignInInfo(models.Model):
    username = models.CharField(max_length=45, unique=True) 
    password = models.CharField(max_length=128)

class MedReg(models.Model):
    supply_id=models.IntegerField(primary_key=True)
    supply_name=models.CharField(max_length=50)
    category=models.CharField(max_length=20)
    unit_price=models.IntegerField()
    num_units=models.IntegerField()
    supplier_id=models.IntegerField()