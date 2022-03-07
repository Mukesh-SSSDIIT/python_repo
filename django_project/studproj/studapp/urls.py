from unicodedata import name
from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('show', views.show,name="show"),
    path('add', views.add,name="add"),
    path('update', views.update,name="update"),
    path('delete/<int:studid>', views.delete,name="delete"),
]