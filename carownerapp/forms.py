from django import forms
from .models import CustomUser

from .models import CarListing

from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm



class SignUpForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')
        
        
        
class LoginForm(AuthenticationForm):
    class Meta:
        fields = ('username', 'password')
        
        
        
class CarListingForm(forms.ModelForm):
    class Meta:
        model = CarListing
        fields = ['make', 'model', 'price', 'image']
        


class ProfilePictureForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['profile_picture']