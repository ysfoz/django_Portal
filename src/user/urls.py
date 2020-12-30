from django.urls import path
from .views import login_user, logout_user, register2

urlpatterns = [
   
    path('register/', register2,name='register'),
    path('login/', login_user,name='login'),
    path('logout/', logout_user,name='logout'),
  
]
