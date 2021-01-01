from django.urls import path
from .views import dashboard,addarticle, detail

urlpatterns = [
   
    path('dashboard/', dashboard,name='dashboard'),
    path('addarticle/', addarticle,name='addarticle'),
    path('article/<int:id>', detail, name='detail')
  
]
