from django.urls import path

from oniBusCompany import views

urlpatterns=[
    path("",views.index,name="viewCompanyHome")
]