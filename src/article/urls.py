from django.urls import path
from django.contrib.auth.decorators import login_required
from .views import dashboard, addarticle, detail, update, delete ,get_articles


urlpatterns = [
   
    path('dashboard/', login_required(dashboard,login_url='/user/login/') ,name='dashboard'),
    path('addarticle/', login_required(addarticle,login_url='/user/login/'),name='addarticle'),
    path('article/update/<int:id>',login_required(update,login_url='/user/login/'),name = 'update'),
    path('article/delete/<int:id>',login_required(delete,login_url='/user/login/'),name='delete'),
    path('article/<int:id>', detail , name='detail'),
    path('',get_articles,name='articles')
  
]
