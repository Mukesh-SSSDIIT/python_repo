from django.shortcuts import render,redirect
from student.models import Book
from student.models import Student
from student.models import Stream

from student.forms import BookForm
from student.forms import StudentForm
from student.forms import StreamForm

def show_book(request):  
    books = Book.objects.all()
    return render(request,"books\\show_book.html",{'books':books}) 

def add_book(request):
    if request.method == "POST":  
        form = BookForm(request.POST)  
        if form.is_valid():  
            try:  
                form.save()  
                return redirect('/')  
            except:
                pass
    else:  
        form = BookForm()  
    return render(request,'books\\add_book.html',{'form':form})

def delete_book(request, id):  
    book = Book.objects.get(id=id)  
    book.delete()
    return redirect("/")

def edit_book(request, id):
    book = Book.objects.get(id=id)  
    return render(request,'books\\edit_book.html', {'book':book})  

def update_book(request, id):  
    book = Book.objects.get(id=id)  
    form = BookForm(request.POST, instance = book)  
    if form.is_valid():  
        form.save()  
        return redirect("/")  
    return render(request, 'books\\edit_book.html', {'book': book})
