from django.contrib import admin
from . models import LoginInfo,SignInInfo,MedReg,Supplier,Medconsume,Medequip

admin.site.register(LoginInfo)
admin.site.register(SignInInfo)
admin.site.register(MedReg)
admin.site.register(Supplier)
admin.site.register(Medconsume)
admin.site.register(Medequip)