from django.shortcuts import render,redirect,HttpResponse
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from .models import LoginInfo,SignInInfo,MedReg,Supplier,Medconsume,Medequip
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password,check_password
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_protect
import uuid


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
    if request.method=="POST":
        sup_name=request.POST.get('sup_name')
        role=request.POST['role']
        supplierid= request.POST.get('supplierid')
        email=request.POST['email']
        phone_no=request.POST.get('phone_no')
        company_name=request.POST.get('company_name')
        company_addr=request.POST.get('company_addr')

        sup_reg=Supplier(supplierid=supplierid,sup_name=sup_name,role=role,email=email,phone_no=phone_no,company_name=company_name,company_addr=company_addr)
        sup_reg.save()
        return render(request, 'users.html', {'success': True})
    
    return render(request,'users.html')

def suppliers(request):
    return render(request,'suppliers.html')

def inventory(request):
    return render(request,'inventory.html')

def medsuppliers(request):
    error_message = None
    if request.method == "POST":
        supply_id = request.POST['supply_id']
        supply_name = request.POST['supply_name']
        category = request.POST['category']
        unit_price = request.POST['unit_price']
        num_units = int(request.POST['num_units'])  
        supplier_id = request.POST['supplier_id']

        try:
            medin = Supplier.objects.get(supplierid=supplier_id)

            if supplier_id != str(medin.supplierid):
                error_message = "Invalid supplier id"
            else:
                if category.strip().lower() == 'equipment':
                    if Medequip.objects.filter(supply_id=supply_id,supply_name=supply_name).exists():
                        medinfo = Medequip.objects.get(supply_id=supply_id)
                        medinfo.num_units += num_units 
                        medinfo.save()
                        return render(request, 'medsuppliers.html', {'success': f'Quantity updated for {medinfo.supply_name}'})
                    else:
                        medinfo = Medequip(supply_id=supply_id, supply_name=supply_name, category=category, unit_price=unit_price, num_units=num_units, supplier_id=medin)
                        medinfo.save()
                        return render(request, 'medsuppliers.html', {'success': 'New equipment entry created'})

                elif category.strip().lower() == 'medication':
                    if MedReg.objects.filter(supply_id=supply_id).exists():
                        medinfo = MedReg.objects.get(supply_id=supply_id)
                        medinfo.num_units += num_units  
                        medinfo.save()
                        return render(request, 'medsuppliers.html', {'success': f'Quantity updated for {medinfo.supply_name}'})
                    else:
                        medinfo = MedReg(supply_id=supply_id, supply_name=supply_name, category=category, unit_price=unit_price, num_units=num_units, supplier_id=medin)
                        medinfo.save()
                        return render(request, 'medsuppliers.html', {'success': 'New medication entry created'})

                else:
                    if Medconsume.objects.filter(supply_id=supply_id).exists():
                        medinfo = Medconsume.objects.get(supply_id=supply_id)
                        medinfo.num_units += num_units 
                        medinfo.save()
                        return render(request, 'medsuppliers.html', {'success': f'Quantity updated for {medinfo.supply_name}'})
                    else:
                        medinfo = Medconsume(supply_id=supply_id, supply_name=supply_name, category=category, unit_price=unit_price, num_units=num_units, supplier_id=medin)
                        medinfo.save()
                        return render(request, 'medsuppliers.html', {'success': 'New consumable entry created'})

        except Supplier.DoesNotExist:
            error_message = "Invalid Supplier id"
        except Exception as e:
            error_message = str(e)

        return render(request, 'medsuppliers.html', {'error_message': error_message})

    return render(request, 'medsuppliers.html')


def log_out(request):
    logout(request)
    return redirect('log_in')

