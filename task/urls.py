
from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.home_view,name ='home'),
    path('bankByIFSC',views.bankByIFSC,name = 'byIFSC'),
    path('bankByNameandCity',views.bankByNameandCity,name= 'byNameCity'),
    ]
