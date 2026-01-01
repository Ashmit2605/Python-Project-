from django.shortcuts import render, redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from .forms import SignupForm, LoginForm

def signup_view(request):
    if request.method=='POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user=form.save(commit=False)    
            user.set_password(form.cleaned_data['password'])
            user.save()
            return redirect('login')
    else:
        form=SignupForm()
    return render(request, 'signup.html', {'form': form})     

def login_view(request):
    if request.method=='POST':
        form=LoginForm(data=request.POST)
        if form.is_valid():
            username=form.cleaned_data.get('username')
            password=form.cleaned_data.get('password')
            user= authenticate(request, username=username ,password=password)
            if user is not None:
                login(request , user)
                return redirect('dashboard')
    else:
        form=LoginForm()
    return render(request, 'login.html',{'form':form})                

def logout_view(request):
    logout(request)
    return redirect('login')  

def dashboard_view(request):
    if not request.user.is_authenticated:
        return redirect('login')
    return render(request,'dashboard.html',{'user':request.user})

def main_page(request):
    return render(request, 'main_page.html')  