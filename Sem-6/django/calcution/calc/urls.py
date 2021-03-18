from django.urls import path
from . import views

urlpatterns = [
    path('', views.showcalc),
    path('result', views.showresult),
]