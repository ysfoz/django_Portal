from django.urls import path
from .views import index,about

urlpatterns = [
   
    path('create/', index,name='create'),
  
]
