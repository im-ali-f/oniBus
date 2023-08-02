from django.shortcuts import render

# Create your views here.
from oniBusApp import forms


def viewIndex(request):
    formObj=forms.searchForm
    if request.method == "POST":
        formObj=forms.searchForm(request.POST)
    return render(request,"index.html",{"searchForm":formObj})
