

import email
from unicodedata import name
from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.urls import reverse_lazy
from matplotlib.style import context
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group,User
from django.contrib.auth.views import PasswordChangeView
from django.contrib.auth.forms import PasswordChangeForm

from .models import *
from .forms import CreateUserForm, PasswordChangingForm, UserUpdateForm, ProfileUpdateForm
from .decorators import unaunthenticated_user, allowed_users, admin_only

# Create your views here.

def index(request):
    return render(request,'index.html')
def about(request):
    return render(request,'about.html')
def courses(request):
    return render(request,'course.html')
def testimonial(request):
    return render(request,'testimonial.html')
def contact(request):
    return render(request,'contact.html')


# @unaunthenticated_user
def register(request):
    
    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')

            group = Group.objects.get(name='customer')
            user.groups.add(group)

            messages.success(request,"Account was successfully created for " + username)
            return redirect('/userprofile')
    else: 
        form = CreateUserForm()
    return render(request,'registration/register.html',{"form":form})

#user profile
def userprofile(request):
    if request.method == "POST":
        fname=request.POST.get('fname')
        lname=request.POST.get('lname')
        email1=request.POST.get('email')
        phone=request.POST.get('phone')
        courses=request.POST.get('course')
        batch=request.POST.get('batch')
        p1=student(firstname=fname,secondname=lname,email=email1,phone=phone,course=courses,batch=batch)
        p1.save()
        return redirect('/login')

    c1=course.objects.all()
    context={'c1':c1}
    return render(request,'registration/userprofile.html',context)

# @unaunthenticated_user
def loginpage(request):
    if request.method == "POST":
        username= request.POST.get('uname')
        password=request.POST.get('pwd')
        #aunthenticating user
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            group = None
            if request.user.groups.exists():
                group=request.user.groups.all()[0].name
        
            if group =='customer':
                return redirect('/studenthome')

            if group == 'admin':
                return redirect('/adminhome')

            if group == 'staff':
                return redirect('staffhome')
            # return redirect('/home')
        else:
            messages.info(request,"Username OR Password is incorrect !")
            return render(request,'registration/login.html')
    return render(request,'registration/login.html')

def logoutuser(request):
    logout(request)
    return redirect('/index')


class PasswordsChangeview(PasswordChangeView):
    # form_class = PasswordChangeForm
    form_class = PasswordChangingForm

    success_url =  reverse_lazy('login')

#homepage for registered user
@login_required(login_url='/login')
def studenthome(request):
    return render(request,'students/studenthome.html')

#homepage for admin
@login_required(login_url='/login')
@allowed_users(allowed_roles=['admin'])
#@admin_only
def adminhome(request):
    return render(request,'adminhome.html')

#homepage for staff
@login_required(login_url='/login')
@allowed_users(allowed_roles=['staff'])
def staffhome(request):
    p1=course.objects.all()
    p2=p1.count()
    s1=student.objects.all()
    s2=s1.count()
    context={'p1':p1,'p2':p2,'s1':s1,'s2':s2}
    return render(request,'staffs/staffhome.html',context)

@login_required(login_url='/login')
@allowed_users(allowed_roles=['staff'])
def addcourse(request):
    if request.method == "POST":
        cid=request.POST.get('courseid')
        cname=request.POST.get('coursename')
        dept=request.POST.get('department')
        duration=request.POST.get('duration')
        fees=request.POST.get('fees')
        p1=course(coursename=cname,courseid=cid,department=dept,duration=duration,fees=fees)
        p1.save()
        return redirect('/staffhome')
    return render(request,'addcourse.html')

#Deleting courses
@login_required(login_url='/login')
@allowed_users(allowed_roles=['staff'])
def delcourse(request,pk_test):
    c1=course.objects.get(id=pk_test)
    c1.delete()    
    return redirect('/staffhome')


#Deleting students
@login_required(login_url='/login')
@allowed_users(allowed_roles=['staff'])
def delstudent(request,pk_test):

    s1=student.objects.get(email=pk_test)
    mail=s1.email
    u1=User.objects.get(email=mail)
    u1.delete()    
    s1.delete()
    return redirect('/staffhome')

@login_required(login_url='/login')
def studentprofile(request,pk_test):
    u1=User.objects.get(id=pk_test)
    s1=student.objects.get(email=u1.email)
    context={'s1':s1}
    return render(request,'students/profile.html',context)

@login_required(login_url='/login')
def profileupdate(request,pk_test):
    if request.method == "POST":
        
        u_form = UserUpdateForm(request.POST,instance=request.user)
        p_form = ProfileUpdateForm(request.POST)

        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request,'Your profile is Updated !')
            return redirect('/studentprofile')
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm()
    u1=User.objects.get(id=pk_test)
    context={'u_form':u_form,'p_form':p_form}
    return render(request,'profile_update.html',context)

def enroll(request,pk_test):
    st1=student.objects.get(id=pk_test)
    c1=course.objects.get(coursename=st1.course)
    s1=c1.fees
    s2=c1.fees
    s3=c1.fees
    s4=c1.fees
    s5=c1.fees
    s6=c1.fees
    total=s1+s2+s3+s4+s5+s6
    f1=fees(sid=st1.id,cid=c1.id,s1=s1,s2=s2,s3=s3,s4=s4,s5=s5,s6=s6,total=total)
    f1.save()
    return redirect('/staffhome')

def viewfee(request,pk_test):
    s1=student.objects.get(id=pk_test)
    sid1=s1.id
    f1=fees.objects.get(sid=s1.id)
    c1=course.objects.get(id=f1.cid)

    context={'s1':s1,'f1':f1,'c1':c1}
    return render(request,'viewfee.html',context)
