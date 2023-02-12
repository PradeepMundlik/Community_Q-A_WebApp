from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login , logout

# Create your views here.
def home(request):
    if(request.user.is_anonymous):
        return redirect('/login')
    return HttpResponse('This is home page')

def create_new_accout(request):
    if(request.method=='POST'):
        password = request.POST.get('password')
        repassword = request.POST.get('repassword')
        username = request.POST.get('username')
        email = request.POST.get('email')
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        if(password==repassword):
            user = User.objects.create_user(username=username,email=email,password=password,first_name=fname,last_name=lname)
            user.save()
            return HttpResponse("Account Created Successfully")
        else:
            return HttpResponse("Passwords are not maatching correctly")
    return render(request,'create_new_account.html')

def Login(request):
    if(request.method=='POST'):
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request,user)
            return redirect('/')
        else:
            return HttpResponse("Invalid Username or Password")
        
    return render(request,'login.html')

def Logout(request):
    logout(request)
    return HttpResponse('This is logout page')
