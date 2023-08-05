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
        {"ticketId":1,"origin":"qazvin","destination":"tehran","busType":"volvo","busOrCompanyImg":"","departure":"20:11","price":"210000","isActive":"active"},
        {"ticketId": 2, "origin": "qazvin", "destination": "tehran", "busType": "volvo","busOrCompanyImg":"", "departure": "20:11","price": "210000", "isActive": "deactive"},
        {"ticketId": 3, "origin": "qazvin", "destination": "tehran", "busType": "volvo","busOrCompanyImg":"", "departure": "20:11","price": "210000", "isActive": "active"},
        {"ticketId": 4, "origin": "qazvin", "destination": "tehran", "busType": "volvo","busOrCompanyImg":"", "departure": "20:11","price": "210000", "isActive": "active"},
        {"ticketId": 5, "origin": "qazvin", "destination": "tehran", "busType": "volvo","busOrCompanyImg":"", "departure": "20:11","price": "210000", "isActive": "deactive"},
    ]
    reqData = request.POST
    context={
        "origin":reqData["originDestination"],
        "destination":reqData["finalDestination"],
        "data":data
    }
    print(context)
    return render(request,"oniBusApp/searchPage.html",context)