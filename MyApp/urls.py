from django.urls import path
from MyApp import views

urlpatterns = [
    path('Myresume/',views.Myresume,name="Myresume")
]