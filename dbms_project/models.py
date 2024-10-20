from django.db import models
from django.core.exceptions import ValidationError
from django.core.validators import MinValueValidator

class LoginInfo(models.Model):
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=128)

class SignInInfo(models.Model):
    username = models.CharField(max_length=45, unique=True) 
    password = models.CharField(max_length=128)

class Supplier(models.Model):
    sup_name=models.CharField(max_length=25)
    role=models.CharField(max_length=25)
    supplierid=models.IntegerField(primary_key=True,unique=True)
    email=models.EmailField(max_length=50)
    phone_no=models.CharField(max_length=25)
    company_name=models.CharField(max_length=50)
    company_addr=models.CharField(max_length=75)


class MedReg(models.Model):
    supply_id=models.IntegerField(primary_key=True)
    supply_name=models.CharField(max_length=50)
    category=models.CharField(max_length=20)
    unit_price=models.DecimalField(max_digits=10, decimal_places=2)
    num_units=models.PositiveIntegerField(default=0)
    supplier_id=models.ForeignKey(Supplier,null=True,on_delete=models.CASCADE)

class Medequip(models.Model):
    supply_id=models.IntegerField(primary_key=True)
    supply_name=models.CharField(max_length=50)
    category=models.CharField(max_length=20)
    unit_price=models.DecimalField(max_digits=10, decimal_places=2)
    num_units=models.PositiveIntegerField(default=0)
    supplier_id=models.ForeignKey(Supplier,null=True,on_delete=models.CASCADE)

class Medconsume(models.Model):
    supply_id=models.IntegerField(primary_key=True)
    supply_name=models.CharField(max_length=50)
    category=models.CharField(max_length=20)
    unit_price=models.DecimalField(max_digits=10, decimal_places=2)
    num_units=models.PositiveIntegerField(default=0)
    supplier_id=models.ForeignKey(Supplier,null=True,on_delete=models.CASCADE)


class Order(models.Model):
    name = models.CharField(max_length=75)
    email = models.EmailField(max_length=50)
    phone = models.CharField(max_length=15)
    item_type = models.CharField(max_length=25)
    item_name = models.CharField(max_length=75)
    quantity = models.IntegerField(validators=[MinValueValidator(1)])

class Product(models.Model):
    name1 = models.CharField(max_length=100)

