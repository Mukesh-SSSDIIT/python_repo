from django.shortcuts import render

# Create your views here.

def showcalc(request):
    return render(request,'calc.html')

def showresult(request):
    n1 = int(request.POST['num1'])
    n2 = int(request.POST['num2'])
    res = n1 + n2
    return render(request,'showresult.html',{'result':res})