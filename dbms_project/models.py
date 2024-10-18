from django.db import models
from django.core.exceptions import ValidationError

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

    # def clean(self):
    #     if not (1000 <= self.supplierid <= 9999):  
    #         raise ValidationError('Supplier ID must be a 4-digit number.')

    # def save(self, *args, **kwargs):
    #     self.clean() 
    #     super(Supplier, self).save(*args, **kwargs)

    # def __str__(self):
    #     return f'{self.sup_name} ({self.supplierid})'

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