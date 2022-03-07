from django.shortcuts import render
from .models import stud
# Create your views here.

def login(request):
    s = stud(first_name="test",last_name="test1",age=50)
    s.save()
    return render(request,'show.html')