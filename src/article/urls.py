from django.urls import path
from .views import dashboard,addarticle

urlpatterns = [
   
    path('dashboard/', dashboard,name='dashboard'),
    path('addarticle/', addarticle,name='addarticle'),
  
]
