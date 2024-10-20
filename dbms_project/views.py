from django.shortcuts import render,redirect,HttpResponse
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from .models import LoginInfo,SignInInfo,MedReg,Supplier,Medconsume,Medequip
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
    if request.method=="POST":
        sup_name=request.POST.get('sup_name')
        role=request.POST['role']
        supplierid= request.POST.get('supplierid')
        email=request.POST['email']
        phone_no=request.POST.get('phone_no')
        company_name=request.POST.get('company_name')
        company_addr=request.POST.get('company_addr')

        if Supplier.objects.filter(supplierid=supplierid).exists():
            return render(request, 'users.html', {'error': True})
        else:
            sup_reg=Supplier(supplierid=supplierid,sup_name=sup_name,role=role,email=email,phone_no=phone_no,company_name=company_name,company_addr=company_addr)
            sup_reg.save()
            return render(request, 'users.html', {'success': True})
    return render(request,'users.html')

def suppliers(request):
    return render(request,'suppliers.html')

def inventory(request):
    return render(request,'inventory.html')

def check_availability(request):
    if request.method == 'POST' and 'check_availability' in request.POST:
        name1 = request.POST.get('name1')
        product = None
        
        try:
            product = MedReg.objects.get(supply_name=name1)
        except MedReg.DoesNotExist:
            try:
                product = Medequip.objects.get(supply_name=name1)
            except Medequip.DoesNotExist:
                try:
                    product = Medconsume.objects.get(supply_name=name1)
                except Medconsume.DoesNotExist:
                    product = None

        if product:
            availability_message = f'{product.supply_name} - Available: {product.num_units} units'
            print("Found")
            return render(request, 'orders.html', {'availability_message': availability_message})
        else:
            error_message = f'No product named "{name1}" is available'
            return render(request, 'orders.html', {'error_message': error_message})

    return render(request, 'orders.html')

def orders(request):
    if request.method == 'POST' and 'place_order' in request.POST:
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        item_type = request.POST.get('item_type')
        item_name = request.POST.get('item_name')

        quantity_str = request.POST.get('quantity')
        
        if not quantity_str or quantity_str.strip() == "":
            error_message = 'Quantity is required.'
            return render(request, 'orders.html', {'error_message': error_message})

        try:
            quantity = int(quantity_str) 
        except ValueError:
            error_message = 'Invalid quantity provided.'
            return render(request, 'orders.html', {'error_message': error_message})

        product = None
        
        try:
            product = MedReg.objects.get(supply_name=item_name)
        except MedReg.DoesNotExist:
            try:
                product = Medequip.objects.get(supply_name=item_name)
            except Medequip.DoesNotExist:
                try:
                    product = Medconsume.objects.get(supply_name=item_name)
                except Medconsume.DoesNotExist:
                    product = None

        if product:
            if product.num_units >= quantity:
                product.num_units -= quantity
                product.save()
                success_message = 'Order placed successfully!'
                return render(request, 'orders.html', {'success_message': success_message})
            else:
                error_message = f'Not enough {product.supply_name} in stock. Only {product.num_units} units available.'
                return render(request, 'orders.html', {'error_message': error_message})
        else:
            error_message = 'The product you requested is not available.'
            return render(request, 'orders.html', {'error_message': error_message})

    return render(request, 'orders.html')



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
                    existing_supplyid = Medequip.objects.filter(supply_id=supply_id).first()
                    existing_supplyname = Medequip.objects.filter(supply_name=supply_name).first()

                    if existing_supplyid and existing_supplyid.supply_name != supply_name:
                        error_message = f'Supply ID {supply_id} already exists with a different name: {existing_supplyid.supply_name}'
                    elif existing_supplyname and existing_supplyname.supply_id != supply_id:
                        error_message = f'Supply Name {supply_name} already exists with a different ID: {existing_supplyname.supply_id}'
                    else :
                        if existing_supplyid:
                            existing_supplyid.num_units += num_units
                            existing_supplyid.save()
                            return render(request, 'medsuppliers.html', {'success': f'Quantity updated for {existing_supplyid.supply_name}'})
                        else:
                            medinfo = Medequip(supply_id=supply_id, supply_name=supply_name, category=category, unit_price=unit_price, num_units=num_units, supplier_id=medin)
                            medinfo.save()
                            return render(request, 'medsuppliers.html', {'success': 'New equipment entry created'})

                elif category.strip().lower() == 'medication':
                    existing_supplyid = MedReg.objects.filter(supply_id=supply_id).first()
                    existing_supplyname = MedReg.objects.filter(supply_name=supply_name).first()

                    if existing_supplyid and existing_supplyid.supply_name != supply_name:
                        error_message = f'Supply ID {supply_id} already exists with a different name: {existing_supplyid.supply_name}'
                    elif existing_supplyname and existing_supplyname.supply_id != supply_id:
                        error_message = f'Supply Name {supply_name} already exists with a different ID: {existing_supplyname.supply_id}'
                    else:
                        if existing_supplyid:
                            existing_supplyid.num_units += num_units
                            existing_supplyid.save()
                            return render(request, 'medsuppliers.html', {'success': f'Quantity updated for {existing_supplyid.supply_name}'})
                        else:
                            medinfo = MedReg(supply_id=supply_id, supply_name=supply_name, category=category, unit_price=unit_price, num_units=num_units, supplier_id=medin)
                            medinfo.save()
                            return render(request, 'medsuppliers.html', {'success': 'New medication entry created'})

                else:
                    existing_supplyid = Medconsume.objects.filter(supply_id=supply_id).first()
                    existing_supplyname = Medconsume.objects.filter(supply_name=supply_name).first()

                    if existing_supplyid and existing_supplyid.supply_name != supply_name:
                        error_message = f'Supply ID {supply_id} already exists with a different name: {existing_supplyid.supply_name}'
                    elif existing_supplyname and existing_supplyname.supply_id != supply_id:
                        error_message = f'Supply Name {supply_name} already exists with a different ID: {existing_supplyname.supply_id}'
                    else:
                        if existing_supplyid:
                            existing_supplyid.num_units += num_units
                            existing_supplyid.save()
                            return render(request, 'medsuppliers.html', {'success': f'Quantity updated for {existing_supplyid.supply_name}'})
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

