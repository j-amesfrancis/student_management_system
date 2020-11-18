from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout

from .decorators import redirect_login, user_redirect


# Create your views here.

@redirect_login
def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            login_error = "Invalid Credentials"
            context = {'login_error': login_error}
            return render(request, 'login.html', context)
    return render(request, 'login.html')


@login_required(login_url='login')
@user_redirect
def home(request):
    return redirect('hod-dashboard')


@login_required(login_url='login')
def user_logout(request):
    logout(request)
    return redirect('login')
