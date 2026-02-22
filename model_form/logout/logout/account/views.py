from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from . forms import Registration_form
from django.contrib.auth.decorators import login_required

def user_registration(request):
    if request.method=='POST':
        form=Registration_form(request.POST)
        if form.is_valid():
            form.save()
            redirect('user_login')
    else:
        form = Registration_form()
    return render(request, 'accounts/register.html', {'form': form})
    
def user_login(request):
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        user= authenticate(request,username=username, password=password)
        if user:
            login(request, user)
            return redirect('dashboard')
    return render(request, 'accounts/login.html')


def user_logout(request):
    logout(request)
    return redirect('user_login')

@login_required(login_url='user_login')
def dashboard(request):
    return render(request, 'accounts/dashboard.html')


