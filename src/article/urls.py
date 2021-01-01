from django.urls import path
from .views import dashboard,addarticle, detail,update,delete, 

urlpatterns = [
   
    path('dashboard/', dashboard,name='dashboard'),
    path('addarticle/', addarticle,name='addarticle'),
    path('article/<int:id>', detail, name='detail'),
    path('article/update/<int:id>',update,name = 'update'),
    path('article/delete/<int:id>',delete,name='delete'),
  
]
