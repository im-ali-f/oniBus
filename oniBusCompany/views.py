from django.shortcuts import render

# Create your views here.
def viewIndex(request):
    return render(request,"oniBusCompany/index.html")
