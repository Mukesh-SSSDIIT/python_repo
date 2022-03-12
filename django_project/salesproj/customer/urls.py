from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('show/', views.showcustomers),
    path('update/', views.updatecustomer,name='updatecustomer'),
]