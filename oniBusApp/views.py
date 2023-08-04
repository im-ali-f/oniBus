from django.shortcuts import render

# Create your views here.
from oniBusApp import forms


def viewIndex(request):
    formObj=forms.searchForm
    if request.method == "POST":
        formObj=forms.searchForm(request.POST)
    return render(request, "oniBusApp/index.html", {"searchForm":formObj})

def viewSearch(request):

    data=[
        {"ticketId":1,"origin":"qazvin","destination":"tehran","busType":"volvo","departure":"20:11","price":"210000","isActive":True},
        {"ticketId": 2, "origin": "qazvin", "destination": "tehran", "busType": "volvo", "departure": "20:11","price": "210000", "isActive": False},
        {"ticketId": 3, "origin": "qazvin", "destination": "tehran", "busType": "volvo", "departure": "20:11","price": "210000", "isActive": True},
    ]
    print(request.POST)
    context={
        "data":data
    }
    return render(request,"oniBusApp/searchPage.html",context)