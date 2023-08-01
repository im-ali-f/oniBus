from django.urls import path
from oniBusApp import views

urlpatterns = [
    path("",views.viewIndex)
]