from django.db import models
from django.contrib.auth.models import User


class BlogPost(models.Model):
    title = models.CharField(max_length=85)
    slug = models.SlugField()
    body_content = models.TextField()
    added_on = models.DateTimeField(auto_now_add=True)
    added_by = models.ForeignKey(User, related_name='blogposts', on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = 'Blog Posts'
    
    def __str__(self):
        return self.title
