from django.shortcuts import render
from .models import car_owner



# Create your views here.
def carowner(request):
    return render(request,'carown/homepage.html',{})

def insertuser(request):
    
    vnumberplate =request.POST['Number_plate']
    vphonenumber=request.POST['Phone_number'] 
    vid=request.POST['ID']
    us= car_owner(Number_plate=vnumberplate, Phone_number=vphonenumber, ID =vid)
    us.save()
    return render(request,'carown/homepage.html',{})
        