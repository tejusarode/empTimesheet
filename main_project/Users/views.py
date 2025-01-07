from django.shortcuts import render,redirect
from .forms import *
from django.contrib import messages
from django.contrib.auth import  authenticate,login

# Create your views here.

def register_view(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST, request.FILES) 
        if form.is_valid():
            try:
                data = form.cleaned_data
                user = RegisterUsers.objects.create_user(
                    emp_id=data['emp_id'],
                    emp_name=data['emp_name'],
                    emp_email=data['emp_email'],
                    emp_phn_number=data['emp_phn_number'],
                    emp_department=data['emp_department'],
                    emp_role=data['emp_role'],
                    password1=data['password1'],
                    password2=data['password2'],
                ) 
                user.save()
                messages.success(request, 'User created successfully! Please log in.')
                return redirect('login')
            except Exception as e:
                messages.error(request, f'Error creating user: {str(e)}')
        else:
            # This will show the form errors in the console or logs
            print("Form errors:", form.errors)
            messages.error(request, 'Form is not valid. Please correct the errors below.',)
    else:
        form = UserRegisterForm
    return render(request, 'register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = authenticate(request, emp_email=data['emp_email'], password=data['password1'])
            if user is not None:
                login(request, user)
                return redirect('home')  
            else:
                messages.error(request, 'Invalid credientials')
                return render(request,"Users/login.html",{'form':form})
    else:
        form = LoginForm()
    return render(request, "login.html", {'form': form})