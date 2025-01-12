from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile

class UserRegisterForm(UserCreationForm):

    email = forms.EmailField(label='Email address', help_text='Your SHU email address.')
    dob = forms.DateField(label='Date of birth')
    address= forms.CharField(label='Address')
    city= forms.CharField(label='City/Town')
    country= forms.CharField(label='Country')

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'dob', 'address', 'city', 'country', 'email', 'password1', 'password2']



class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()
    email = forms.EmailField(label='Email address', help_text='Your SHU email address.')
    dob = forms.DateField(label='Date of birth')
    address= forms.CharField(label='Address')
    city= forms.CharField(label='City/Town')
    country= forms.CharField(label='Country')

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'dob', 'address', 'city', 'country', 'email']

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image']
