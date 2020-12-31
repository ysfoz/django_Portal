
from django.shortcuts import render, redirect
from .forms import RegisterForm, LoginForm, CreateUserForm
from django.contrib import messages

from django.contrib.auth.models import User
from django.contrib.auth import login,logout,authenticate
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


# 2. yontem
# def register(request):
#    form = RegisterForm(request.POST or None)
#    if form.is_valid():
#        username = form.cleaned_data.get('username')
#        password = form.cleaned_data.get('password')
#        user = User(username=username)
#        user.set_password(password)
#        user.save()
#        login(request, user)
#        messages.success(request,'You signed in successfully')
#        return redirect('index')
#    context = {
#        'form':form
#    }
   
#    return render(request,'register.html',context)
       
        


# def login_user2(request):
#     form = LoginForm(request.POST or None)
#     context = {
#         'form':form
#     }
#     if form.is_valid:
#         username = form.cleaned_data.get('username')
#         password = form.cleaned_data.get('password')
        
#         user = authenticate(username = username, password= password)
        
#         if user is None:
#             messages.warning(request,'Username or Password is incorrect')
#             return render(request,'login.html', context)
        
#         messages.success(request, 'you loged in successfuly')
    
#     return render(request,'login.html', context)
    
        
def login_user(request):
    form = LoginForm()
    context = {
            'form':form
              }
    if request.method == 'POST':
        
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username = username, password = password)
        if user is not None:
            login(request,user)
            messages.success(request,'you loged in successfuly')
            return redirect('index')
        messages.warning(request,'Username or Password is incorrect')
        return render(request,'login.html',context)
    return render(request,'login.html',context)
    
    
     

def logout_user(request):
    logout(request)
    messages.success(request,'you loged out succesfuly')
    return redirect('index')


def register2(request):
    form = CreateUserForm(request.POST or None)
    if form.is_valid():
        form.save()
        user = form.cleaned_data.get('username')
        messages.success(request,'You signed in successfully' + ' ' + user)
        return redirect('login')
    context ={
        'form':form
    }
    return render(request,'register.html',context)
    