from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.
class Article(models.Model):
    author = models.ForeignKey('auth.user',on_delete=models.CASCADE,verbose_name='yazar')
    title = models.CharField(max_length=50)
    content = RichTextField()
    created_date = (models.DateTimeField(auto_now_add=True))
    def __str__(self):
        return self.title
    