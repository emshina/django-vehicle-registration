from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Registration
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib import auth
from django.db import connection
from django.utils.text import slugify

# def my_custom_sql(request):
#     with connection.cursor() as cursor:
#         cursor.execute("SELECT * FROM car_owner")
#         rows = cursor.fetchall()
        
#     return render(request,'carown/police.html',{'rows':rows})


# def charges(request):
#     Number_Plate = request.GET.get('id','Not available')
#     if(Number_Plate != 'Not available'):
#         with connection.cursor() as cursor:
#             cursor.execute("SELECT * FROM car_owner WHERE Number_Plate = %s",[Number_Plate])
#             rows = cursor.fetchall()

#         return render(request,'carown/display.html',{'st': st})
#     else:
#         st = Registration.objects.all()
#         return render(request,'carown/list.html',{'st': st})
  
        
# # # Create your views here.
def carowner(request):
    return render(request,'carown/home.html',{})

def registration(request):
   
    if request.method == 'POST':
    
        if request.POST['Number_plate']== '' or request.POST['email']=='':
            messages.error(request,'Include all fields')
        else:
            numberplate =request.POST['Number_plate']
            vnumberplate = numberplate.replace(' ', '').lower()
            vemail=request.POST['email'] 
            vid=request.POST['ID']
            us= Registration(Number_Plate=vnumberplate, email=vemail, ID_id=vid)
            us.save()
            messages.success(request,'registration successful.')

    return render(request,'carown/registration.html',{})

def display(request):
    # records = registration.objects
    
    st = Registration.objects.all()
    return render(request,'carown/display.html',{'st':st})

# def display2(request):
#     # Number_Plate = request.GET.get('Number_Plate','Not available')
#     # # n= Number_Plate.replace(' ', '')
#     # if(Number_Plate != 'Not available'):
#     #     with connection.cursor() as cursor:
#     #         cursor.execute("SELECT REPLACE(Number_Plate, ' ', '') AS correct_Number_Plate, ID, Phone_Number FROM car_owner correct_WHERE Number_Plate = %s",[Number_Plate])
#     #         rows = cursor.fetchall()
#     #     return HttpResponse(rows)

#     #     # return render(request,'carown/display.html',{'rows': rows})
#     # else:
#     #     with connection.cursor() as cursor:
#     #         cursor.execute("SELECT Number_Plate FROM car_owner")
#     #         rows = cursor.fetchall()
#     #     # return HttpResponse(rows)
            
            
            
#         # return render(request,'carown/list.html',{'rows':rows})
#     Number_Plate = request.GET.get('Number_Plate','Not available')
#     n= Number_Plate.replace(' ', '')
#     if(Number_Plate != 'Not available'):
#         with connection.cursor() as cursor:
#             cursor.execute("SELECT * FROM car_owner WHERE ID = %s",[Number_Plate])
#             rows = cursor.fetchall()
#         return HttpResponse(rows)

#         return render(request,'carown/display.html',{'rows': rows})
#     else:
#         with connection.cursor() as cursor:
#             cursor.execute("SELECT ID FROM car_owner")
#             rows = cursor.fetchall()
            
#         return render(request,'carown/list.html',{'rows':rows})

    
def signup(request):
    if request.method == "POST":
        if request.POST['password1'] == request.POST['password2']:
            try:
                User.objects.get(username = request.POST['username'])
                return render (request,'carown/signup.html', {'error':'Username is already taken!'})
            except User.DoesNotExist:
                user = User.objects.create_user(request.POST['username'],password=request.POST['password1'])
                auth.login(request,user)
                return redirect('../login/')
        else:
            return render (request,'carown/signup.html', {'error':'Password does not match!'})
    else:
        return render(request,'carown/signup.html')

def login(request):
    if request.method == 'POST':
        user = auth.authenticate(username=request.POST['username'],password = request.POST['password'])
        if user is not None:
            k= auth.login(request,user)
            return redirect('../list/',{'k':k})
        else:
            return render (request,'carown/login.html', {'error':'Username or password is incorrect!'})
    else:
        return render(request,'carown/login.html')
