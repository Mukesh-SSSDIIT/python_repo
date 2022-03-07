from django.http import HttpResponse
from django.shortcuts import redirect, render
from .models import stud
# Create your views here.

def show(request):
    students = stud.objects.all()
    return render(request,'show.html',
                            {'students':students})

def add(request):
    if request.method == "POST":
        v_first_name = request.POST["first_name"]
        v_last_name = request.POST["last_name"]
        v_age = request.POST["age"]
        s = stud(first_name=v_first_name,last_name=v_last_name,
                                                age = v_age)
        s.save()
        return redirect('show')
    else:
        return render(request,"add.html")

def update(request):
    if request.method == "POST":
        v_id = request.POST["id"]
        v_first_name = request.POST["first_name"]
        v_last_name = request.POST["last_name"]
        v_age = request.POST["age"]
        s = stud.objects.get(id=v_id)
        s.first_name = v_first_name
        s.last_name = v_last_name
        s.age = v_age
        s.save()
        return redirect('show')
    else:
        studid = request.GET['studid']
        s=stud.objects.get(id=studid)
        return render(request, "update.html",{"stud":s})

def delete(request, studid):
    s=stud.objects.get(id=studid)
    s.delete()
    return redirect('show')