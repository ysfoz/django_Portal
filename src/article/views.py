from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render, get_object_or_404
from.forms import ArticleForm
from django.contrib import messages
from .models import Article




# Create your views here.

def index(request):
   return render(request,'index.html')

def about(request):
   return render(request, 'about.html')
login_required(login_url='addarticle')
def dashboard(request):
   articles = Article.objects.filter(author = request.user)
   context = {
      'articles':articles
   }
   return render(request, 'dashboard.html',context)

def addarticle(request):
   form = ArticleForm(request.POST or None, request.FILES or None)
   if form.is_valid():
      article = form.save(commit=False)
      article.author = request.user
      article.save()
      messages.success(request,'You added an article successfuly')
      return redirect('dashboard')
   context = {
      'form':form
   }
   return render(request, 'addarticle.html',context)

def detail(request,id):
   # article = Article.objects.filter(id=id) # buraya .first() yazarsak html sayfasinda for dongusune gerek kalmiyor
   article = get_object_or_404(Article, id = id)
   context = {
      'article': article
   }
   return render(request, 'detail.html',context)

def update(request,id):
   article =get_object_or_404(Article,id=id)
   form = ArticleForm(request.POST or None,request.FILES or None ,instance=article)
   if form.is_valid():
      article = form.save(commit=False)
      article.author = request.user
      article.save()
      messages.success(request,'You updated an article successfuly')
      return redirect('dashboard')
   context ={
      'form':form
   }
   return render(request,'update.html',context)
      
   
def delete(request,id):
   article = get_object_or_404(Article,id=id)
   if request.method == 'POST':
      article.delete()
      messages.success(request,'you deleted the article')
      return redirect('dashboard')
   context ={
      'article':article
   }   
   return render(request,'delete.html',context)

def get_articles(request):
   keyword =request.GET.get('keyword')
   
   if keyword:
      articles =Article.objects.filter(title__contains = keyword)
      context ={
      'articles':articles
   }
      return render(request,'articles.html',context)
   articles = Article.objects.all()
   context ={
      'articles':articles
   }
   return render(request,'articles.html',context)