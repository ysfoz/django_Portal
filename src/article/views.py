from django.shortcuts import render


# Create your views here.

def index(request):
   return render(request,'index.html')

def about(request):
   return render(request, 'about.html')

def dashboard(request):
   return render(request, 'dashboard.html')

def addarticle(request):
   return render(request, 'addarticle.html')
   