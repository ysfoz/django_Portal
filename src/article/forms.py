from django import forms
from django.forms import fields

from article.models import Article



class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['title','content','article_image']