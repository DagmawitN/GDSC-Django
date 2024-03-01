from django.db import models

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=255, unique=True)
    content = models.TextField()
    category = models.CharField(max_length=255)
    image = models.ImageField(upload_to='post_images')
    tags = models.CharField(max_length=255)

    def __str__(self):
        return self.title