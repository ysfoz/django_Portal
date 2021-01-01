from django.urls import path
from django.contrib.auth.decorators import login_required
from .views import dashboard, addarticle, detail, update, delete


urlpatterns = [
   
    path('dashboard/', login_required(dashboard,login_url='/user/login/') ,name='dashboard'),
    path('addarticle/', login_required(addarticle,login_url='/user/login/'),name='addarticle'),
    path('article/<int:id>', login_required(detail,login_url='/user/login/'), name='detail'),
    path('article/update/<int:id>',login_required(update,login_url='/user/login/'),name = 'update'),
    path('article/delete/<int:id>',login_required(delete,login_url='/user/login/'),name='delete'),
  
]
