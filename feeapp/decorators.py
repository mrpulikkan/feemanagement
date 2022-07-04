from ast import Return
from tokenize import group
from django.http import HttpResponse
from django.shortcuts import redirect

def unaunthenticated_user(view_func):
    def wrapper_fun(request, *args, **kwargs):
        if request.user.is_authenticated:
            return HttpResponse("You are already logged in !")
        else:
            return view_func(request, *args, **kwargs)

    return wrapper_fun 

def allowed_users(allowed_roles=[]):
    def decorator(view_func):
        def wrapper_func(request, *args, **kwargs):

            group = None
            if request.user.groups.exists():
                group=request.user.groups.all()[0].name
            if group in allowed_roles:
                return view_func(request, *args, **kwargs)
            else:
                return HttpResponse("You are not authorized to this page")
        return wrapper_func
    return decorator

def admin_only(view_func):
    def wrapper_func(request, *args, **kwargs):
        group = None
        if request.user.groups.exists():
            group=request.user.groups.all()[0].name
        
        if group =='customer':
            return redirect('/home')
           
        if group == 'admin':
            return redirect('/adminhome')

    return wrapper_func


