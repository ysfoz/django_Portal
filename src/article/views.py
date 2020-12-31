from django.shortcuts import redirect, render
from.forms import ArticleForm
from django.contrib import messages
from .models import Article


# Create your views here.

def index(request):
   return render(request,'index.html')

def about(request):
   return render(request, 'about.html')

def dashboard(request):
   articles = Article.objects.filter(author = request.user)
   context = {
      'articles':articles
   }
   return render(request, 'dashboard.html',context)

def addarticle(request):
   form = ArticleForm(request.POST or None)
   if form.is_valid():
      article = form.save(commit=False)
      article.author = request.user
      article.save()
      messages.success(request,'You added an article successfuly')
      return redirect('index')
   context = {
      'form':form
   }
   return render(request, 'addarticle.html',context)
   