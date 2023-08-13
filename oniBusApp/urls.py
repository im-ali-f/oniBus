from django.urls import path
from oniBusApp import views

urlpatterns = [
    path("",views.viewIndex),
    path("searchPage",views.viewSearch,name="searchPage"),
    path("searchPage/<ticketId>",views.viewSpecific,name="specificSearchPage")
]