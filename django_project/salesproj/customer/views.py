from django.http import HttpResponse
from django.shortcuts import render
from .models import customer
# Create your views here.

def showcustomers(request):
    customers = customer.objects.all()
    return render(request,'showcustomer.html',{"cust":customers})

def updatecustomer(request):
    cust_id = request.GET['cid']
    r = customer.objects.get(id=cust_id)
    return render(request,'updatecustomer.html',{"cust":r})