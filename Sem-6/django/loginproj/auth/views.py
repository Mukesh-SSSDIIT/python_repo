from django.http.response import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def login(request):
    return render(request,'login.html')

def forgetpassword(request):
    return render(request,'forgetpassword.html')

def verifylogin(request):
    username = request.POST['username']
    password = request.POST['password']
    if username == 'india' and password == 'india123':
        return render(request,'welcome.html')
    else:
        errormessage = "Not a valid username or password"
        return render(request,'login.html',{'errormessage':errormessage})