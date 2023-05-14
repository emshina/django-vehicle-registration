from django.shortcuts import render,redirect
from .models import car_owner
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib import auth



# Create your views here.
def carowner(request):
    return render(request,'carown/home.html',{})

def insertuser(request):
   
    if request.method == 'POST':
    
        if request.POST['Number_plate']== '' or request.POST['Phone_number'] or request.POST['ID']:
            messages.error(request,'registration error')
        else:
            vnumberplate =request.POST['Number_plate']
            vphonenumber=request.POST['Phone_number'] 
            vid=request.POST['ID']
            us= car_owner(Number_plate=vnumberplate, Phone_number=vphonenumber, ID =vid)
            us.save()
            messages.success(request,'registration successful.')

    return render(request,'carown/homepage.html',{})

def display(request):
    st = car_owner.objects.all()
    return render(request,'carown/display.html',{'st':st})

def display2(request):
    id = request.GET.get('id','Not available')
    if(id != 'Not available'):
        st= car_owner.objects.get(ID= id)
        return render(request,'carown/display.html',{'st': st})
    else:
        st = car_owner.objects.all()
        return render(request,'carown/list.html',{'st': st})
    
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
