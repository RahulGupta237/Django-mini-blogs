from cProfile import label
from dataclasses import fields
from pyexpat import model
from tkinter import Widget
from django.contrib.auth.forms import UserCreationForm,UserChangeForm
from django.contrib.auth.models import User
from django import forms

from .models import post

class SignUpForm(UserCreationForm):
    password1=forms.CharField(label='Password',widget=forms.PasswordInput())
    password2=forms.CharField(label='confirm password(again)',widget=forms.PasswordInput())
    class Meta:
        model=User
        fields=['username','first_name','last_name','email']
        labels={'email':"Email","first_name":"First Name","last_name":"Last Name","username":"User Name"}
        Widgets={

            'username':forms.TextInput(attrs={'class':'form-control'}),
               'first_name':forms.TextInput(attrs={'class':'form-control'}),
                  'last_name':forms.TextInput(attrs={'class':'form-control'}),
                    'email':forms.EmailInput(attrs={'class':'form-control'})
        }

class PostForm(forms.ModelForm):
    class Meta:
        model=post
        fields=['title','description']
        labels={'title':'Title','description':'Description'}
        Widgets={
            'title':forms.TextInput(attrs={'class':'form-control'}),
            'description':forms.Textarea(attrs={'class':'form-control'})
        }