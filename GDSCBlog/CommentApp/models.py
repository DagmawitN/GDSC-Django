from django.db import models

# Create your models here.
from BlogApp.models import Post
from django.utils import timezone

class Comment(models.Model):
    content = models.TextField()
    author = models.CharField(max_length=255)
    published_date = models.DateTimeField(default=timezone.now)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)

    def __str__(self):
        return self.content