
from pyexpat import model
from attr import field, fields
from django.contrib.auth.forms import UserCreationForm,PasswordChangeForm
from django.contrib.auth.models import User
from django import forms

from feeapp.models import student

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email','password1','password2']

#password changing form extended from default django form
class PasswordChangingForm(PasswordChangeForm):
    old_password: forms.CharField(max_length=50, widget=forms.PasswordInput(attrs={'class':'form-control'}))
    new_password1: forms.CharField(max_length=50, widget=forms.PasswordInput(attrs={'class':'form-control'}))
    new_password2: forms.CharField(max_length=50, widget=forms.PasswordInput(attrs={'class':'form-control'}))

    class Meta:
        model = User
        fields = ('old_password','new_password1','new_password2')

#user profile updating form
class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model  = User
        fields = ['username','email']
class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = student
        fields = '__all__'
     