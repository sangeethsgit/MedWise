from django.shortcuts import render,redirect,HttpResponse
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from .models import LoginInfo,SignInInfo,MedReg
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password,check_password
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_protect


def log_in(request):
    error_message = None
    if request.method == "POST":
        uname = request.POST['username']
        pass1 = request.POST['password']
        
        try:
            user1 = SignInInfo.objects.get(username=uname) 
            if check_password(pass1, user1.password):  
                return redirect('home')
            else:
                error_message = "Invalid password."
        except SignInInfo.DoesNotExist:
            error_message = "User does not exist."

    return render(request, 'login.html', {'error_message': error_message})



def sign_up(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']

        if SignInInfo.objects.filter(username=username).exists():
            return render(request, 'signup1.html', {'existing_user': True})

        if password == confirm_password:
            hashed_password = make_password(password)
            signinfo = SignInInfo(username=username, password=hashed_password)
            signinfo.save()
            return redirect('log_in')
        else:
            return render(request, 'signup1.html', {'password_mismatch': True})

    return render(request, 'signup1.html')

#@login_required(login_url='log_in')
def home(request):
    return render(request,'home.html')

def users(request):
    return render(request,'users.html')

def suppliers(request):
    return render(request,'suppliers.html')

def inventory(request):
    return render(request,'inventory.html')

def medsuppliers(request):
    if request.method== "POST":
        supply_id= request.POST['supply_id']
        supply_name =request.POST['supply_name']
        category= request.POST['category']
        unit_price= request.POST['unit_price']
        num_units= request.POST['num_units']
        supplier_id= request.POST['supplier_id']

        if MedReg.objects.filter(supply_id=supply_id).exists():
            return render(request, 'medsuppliers.html', {'existing_med': True})
        
        medinfo = MedReg(supply_id=supply_id,supply_name=supply_name,category=category,unit_price=unit_price,num_units=num_units,supplier_id=supplier_id)
        medinfo.save()
        return render(request, 'medsuppliers.html', {'success': True})

        
    return render(request,'medsuppliers.html')

def log_out(request):
    logout(request)
    return redirect('log_in')

