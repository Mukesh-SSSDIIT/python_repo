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
            return redirect("login")
    else:
        return render(request,"login.html")

def logout(request):
    del request.session['username']
    return redirect('login')