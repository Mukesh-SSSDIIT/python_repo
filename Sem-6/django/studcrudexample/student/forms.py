from django import forms  
from student.models import Student
class StudentForm(forms.ModelForm):  
    class Meta:  
        model = Student
        fields = "__all__"

class StreamForm(forms.ModelForm):
    class Meta:
        model = "Stream"
        fields = "__all__"