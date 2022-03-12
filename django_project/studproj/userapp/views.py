from django.shortcuts import redirect, render
from .models import users
# Create your views here.

def login(request):
    if request.method == 'POST':
        v_username = request.POST['username']
        v_password = request.POST['password']
        try:
            u = users.objects.get(username=v_username,password=v_password)
            request.session['username'] = v_username
            return redirect('show')
        except:
            return render(request,"login.html",
                    {'invaliduser':'invalid user or password'})
    else:
        return render(request,"login.html")

def logout(request):
    del request.session['username']
    return redirect('login')

def register(request):
    if request.method == 'POST':
        v_username = request.POST['username']
        v_password = request.POST['password']
        v_retype_password = request.POST['retype_password']
        
        if v_password == v_retype_password:
            try:
                users.objects.get(username=v_username)
                return render(request,'register.html',{'invaliduser':'User alread exists'})
            except:
                u = users(username=v_username,password=v_password)
                u.save()
                return render(request,"login.html")
        else:
            return render(request,'register.html',{'invaliduser':'Password and retype password does not match'})
    else:
        return render(request,"register.html")