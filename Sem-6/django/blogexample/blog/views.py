from django.shortcuts import render
from blog.models import Blog
# Create your views here.
def show(request):
    # Create New Record - Method 1
    # b= Blog(name="Secondblog",tagline="Java")
    # b.save()

    # Create New Record - Method 2
    # b = Blog.objects.create(name="Third Blog", tagline="C++")

    # Update Record
    # blog = Blog.objects.get(id=1)
    # blog.name = "Namechanged"
    # blog.save()

    # Delete Record
    # blog = Blog.objects.get(id=1)
    # blog.delete()

    blogs = Blog.objects.all()

    # blogs = Blog.objects.filter(id=3)

    return render(request,'show.html',{'blogs':blogs})