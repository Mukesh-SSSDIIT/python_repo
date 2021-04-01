from django import forms  
from student.models import Student
from student.models import Stream
from student.models import Book

class StudentForm(forms.ModelForm):  
    class Meta:  
        model = Student
        fields = "__all__"

class StreamForm(forms.ModelForm):
    class Meta:
        model = Stream
        fields = "__all__"

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = "__all__"