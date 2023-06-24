from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Registration
from django.contrib import messages
from .forms import ProfilePictureForm

from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.decorators import login_required

from .forms import SignUpForm, CarListingForm, LoginForm
from django.contrib import messages
from .models import CarListing, CustomUser
from .forms import SignUpForm




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


    

# @login_required
def signup_view(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            profile_picture = user.profile_picture
            messages.success(request, 'Account created for ' + user)
            # Redirect to the success page or login page
            return redirect('login')
    else:
        form = SignUpForm()
    return render(request, 'carown/signup.html', {'form': form , 'user': user, 'profile_picture': profile_picture})



# @login_required
def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                # Redirect to the dashboard or any desired page
                return redirect('dashboard')
            else:
                form.add_error(None, 'Invalid username or password')
    else:
        form = LoginForm()
    return render(request, 'carown/login.html', {'form': form})

@login_required
def logout_view(request):
    logout(request)
    return redirect('login')


@login_required
def dashboard(request):
    if request.method == 'POST':
        form = CarListingForm(request.POST, request.FILES)
        if form.is_valid():
            car_listing = form.save(commit=False)
            car_listing.user = request.user
            
            car_listing.save()
            return redirect('dashboard')
            
            
        Profile_PictureForm = ProfilePictureForm(request.POST, request.FILES)
        if Profile_PictureForm.is_valid():
            
           Profile_PictureForm = Profile_PictureForm.save(commit=False)
           Profile_PictureForm.user = request.user
           
           Profile_PictureForm.save()
           return redirect('dashboard')  # Redirect to the user's profile page
    else:
        form = CarListingForm()
        Profile_PictureForm  = ProfilePictureForm()
    # user = form.cleaned_data.get('username')

    car_listings = CarListing.objects.filter(user = request.user)
    for_sell = CarListing.objects.all()
    
    profilepic = CustomUser.objects.filter(user = request.user)
    context = {
        'form': form,
        'Profile_PictureForm': Profile_PictureForm ,
        'car_listings': car_listings,
        'for_sell': for_sell,
        'profilepic': profilepic
    }
    return render(request, 'carown/dashboard.html', context)





