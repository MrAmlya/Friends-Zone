from .models import Post

from django import forms

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ['title', 'text','hotel_Main_Img',]

class SignUpForm(UserCreationForm):
    email = forms.EmailField(max_length=200, help_text="Enter Your Offitial Email")
    first_name = forms.CharField(max_length=15, label='First name')
    last_name = forms.CharField(max_length=15, label='Last name')

    class Meta:
        model = User
        fields = ['username', 'email','first_name' ,'last_name', 'password1', 'password2',]        

from django import forms 
from .models import *
  
class HotelForm(forms.ModelForm): 
  
    class Meta: 
        model = Gallery 
        fields = ['name', 'hotel_Main_Img'] 