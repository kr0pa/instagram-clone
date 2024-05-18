from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=300)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='app_posts')
    body = models.TextField()
    image = models.ImageField(blank=True)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['-created']
    
    def __str__(self):
        return self.title