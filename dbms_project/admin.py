from django.contrib import admin
from . models import LoginInfo,SignInInfo,MedReg

admin.site.register(LoginInfo)
admin.site.register(SignInInfo)
admin.site.register(MedReg)