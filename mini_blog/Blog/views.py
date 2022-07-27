from tokenize import group
from turtle import title
from unicodedata import name
from django.shortcuts import render,HttpResponseRedirect

# Create your views here.
from .forms import SignUpForm,PostForm

from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm,PasswordChangeForm,SetPasswordForm,UserChangeForm
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User,Group
from .models import post


def home(request):
    data=post.objects.all()
    return render(request,'Blog/home.html',{"post":data})

def about(request):
    return render(request,'Blog/about.html')


def contact(request):
    return render(request,'Blog/contact.html')





def user_signup(request):
    fm=SignUpForm()

    if request.method=="POST":
        fm=SignUpForm(request.POST)
        if fm.is_valid():
            user_new=fm.save()

            group=Group.objects.get(name='Author')
            user_new.groups.add(group)


            print("data successfullya saved")
            messages.success(request,"Congratullation your account successfully created")
            return HttpResponseRedirect('/ogin/')

    else:
        if request.user.is_authenticated:
            logout(request)
        else:
            fm=SignUpForm()
            print("get the form data")


    return render(request,'Blog/signup.html',{"forms":fm})



def dashboard(request):
    if request.user.is_authenticated:
        posts=post.objects.all()
        user=request.user
        full_name=user.get_full_name()
        gps=user.groups.all()

        return render(request,'Blog/dashboard.html',{'post':posts,'name':full_name,'group':gps})



def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/about/')








def user_login(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect('/dashboard/')
    
    else:
        if request.method=='POST':
            fm=AuthenticationForm(request=request,data=request.POST)
            if fm.is_valid():
                uname=fm.cleaned_data['username']
                upass=fm.cleaned_data['password']
                user=authenticate(username=uname,password=upass)
                if user is not None:
                    #login(request,user)
                    login(request, user, backend='django.contrib.auth.backends.ModelBackend')
                    print("i am login rahul")
                    messages.success(request,"successfully login")
                    return HttpResponseRedirect('/dashboard/')
                else:
                    print("you are fake")
                    messages.error(request,f"wrong credential for {uname}")
        else:
            fm=AuthenticationForm()
        return render(request,'Blog/login.html',{"forms":fm})



def add_post(request):
    if request.user.is_authenticated:
        if request.method=='POST':
            add_post=PostForm(request.POST)
            if add_post.is_valid():
                title=add_post.cleaned_data['title']
                desc=add_post.cleaned_data['description']
                pst=post(title=title,description=desc)
                pst.save()
                messages.success(request,'Successfully post addedd')
                return HttpResponseRedirect('/dashboard/')
        else:
            add_post=PostForm()
        return render(request,'Blog/add.html',{'forms':add_post})

    else:
        return HttpResponseRedirect('/ogin/')





def update_post(request,id):
    if request.user.is_authenticated:
        
        if request.method=='POST':
            pi=post.objects.get(pk=id)
            update_post=PostForm(request.POST,instance=pi)
            if update_post.is_valid():
                # title=update_post.cleaned_data['title']
                # desc=update_post.cleaned_data['description']
                # pst=post(title=title,description=desc)
                update_post.save()
                messages.success(request,'Successfully post Edited')
                return HttpResponseRedirect('/dashboard/')
        else:
            pi=post.objects.get(pk=id)
            update_post=PostForm(instance=pi)
        return render(request,'Blog/update.html',{'forms':update_post})

    else:
        return HttpResponseRedirect('/ogin/')



def delete_post(request,id):
    if request.user.is_authenticated:
         
        
        if request.method=='POST':
            pi=post.objects.get(pk=id)
            pi.delete()
            messages.success(request,'Successfully deleted')
            return HttpResponseRedirect('/dashboard/')

    else:
        return HttpResponseRedirect('/ogin/')