from django.db import models
from django.conf import settings
# Create your models here.
## qna, 고민나누기, 중고장터, 동네사람들, 기타

article_category = [
    ("Q&A", "Q&A"),
    ("고민나누기", "고민나누기"),
    ("중고장터", "중고장터"),
    ("동네사람들", "동네사람들"),
    ("기타", "기타"),
]

class Article(models.Model):
  user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete = models.CASCADE)
  like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_article')
  Category = models.CharField(max_length = 5, choices = article_category)
  title = models.CharField(max_length=15)
  content = models.TextField()
  content_img = models.ImageField(upload_to='community_images/', blank=True, null=True)
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)
  
class Comment(models.Model):
  article = models.ForeignKey(Article, on_delete = models.CASCADE)
  user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete = models.CASCADE)
  content = models.CharField(max_length=100)
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)