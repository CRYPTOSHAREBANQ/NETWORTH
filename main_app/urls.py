from django.urls import path
from . import views

app_name = "atm_functions"
urlpatterns = [

     path("EstateNetWorth/", views.estate_net_worth, name="EstateNetWorth"),
     path("EditEstateNetWorth/", views.edit_estate_net_worth, name="EditEstateNetWorth"),
]