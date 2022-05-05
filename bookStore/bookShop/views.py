from pyexpat.errors import messages
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login as auth_login, authenticate, logout as log
from django.contrib.auth.models import User
# Create your views here.

def auth(request):
    return render(request,'bookShop/login_signup.html',{})

@login_required
def home(request):
    return render(request,'bookShop/index.html',{})

@login_required    
def syllabus(request):
    return render(request,'bookShop/syllabus.html',{})

@login_required
def notes(request):
    return render(request,'bookShop/notes.html',{})

@login_required
def manuals(request):
    return render(request,'bookShop/manual.html',{})

@login_required
def books(request):
    return render(request,'bookShop/book.html',{})

def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        email = request.POST.get('email')
        user = User.objects.create_user(username,email,password)
        # print("\n"+username+" "+password+" "+email+"\n")
        user.save()
        return redirect('home')
    else:
        return redirect('auth')

def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username = username, password = password)
        # print("\n"+username+" "+password+"\n")
        if user is not None:
            auth_login(request, user)
            return redirect('home')
        else:
            return redirect('auth')
    else:
        return redirect('auth')   

@login_required
def logout(request):
    log(request)
    return redirect('auth')
