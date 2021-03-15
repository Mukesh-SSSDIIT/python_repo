from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def calc(request):
    #val1 = request.
    #return HttpResponse("Hello world")
    val1 = int(request.GET['num1'])
    val2 = int(request.GET['num2'])
    res = val1 + val2
    return render(request, 'result.html', {'result':res})

def home(request):
    #return HttpResponse("This is home page")
    return render(request,'home.html',{'name':'Ajay'})