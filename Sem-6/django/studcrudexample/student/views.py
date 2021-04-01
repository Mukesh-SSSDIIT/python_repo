from django.shortcuts import render,redirect
from student.models import Book
from student.models import Student
from student.models import Stream

from student.forms import BookForm
from student.forms import StudentForm
from student.forms import StreamForm

def show_book(request):  
    books = Book.objects.all()
    return render(request,"books\show_book.html",{'books':books}) 

# Create your views here.
