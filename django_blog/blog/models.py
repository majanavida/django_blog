from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250, unique=True)
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    
    
    class Meta:
        ordering = ['-created']
        indexes = [
            models.Index(fields=['-created'])
        ]
    
    
    def __str__(self):
        return self.title