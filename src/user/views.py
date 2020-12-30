
from django.shortcuts import render, redirect
from .forms import RegisterForm

from django.contrib.auth.models import User
from django.contrib.auth import login
# Create your views here.



# 1. yöntem
# def register(request):
#     if request.method == 'POST':
#         form = RegisterForm(request.POST)
#         if form.is_valid():
#             username = form.cleaned_data.get('username')
#             password = form.cleaned_data.get('password')

#             user = User(username=username)
#             user.set_password(password)
#             user.save()
#             login(request, user)
#             return redirect('index')
#         context = {
#         'form': form
#         }
#         return render(request, 'register.html', context)

#     else:
#         form = RegisterForm()
#         context = {
#             'form': form
#         }
#         return render(request, 'register.html', context)

def register(request):
   form = RegisterForm(request.POST or None)
   if form.is_valid():
       username = form.cleaned_data.get('username')
       password = form.cleaned_data.get('password')
       user = User(username=username)
       user.set_password(password)
       user.save()
       return redirect('index')
   context = {
       'form':form
   }
   
   return render(request,'register.html',context)
       
        


def login_user(request):
    return render(request, 'login.html')


def logout_user(request):
    return render(request, 'logout.html')
