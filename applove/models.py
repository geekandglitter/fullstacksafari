# When this file is edited, it must be followed by a makemigrations and then a migrate
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
# Below are the model fields
class Post(models.Model):
    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('published', 'Published'),
    )
    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250, unique_for_date='publish')
    # Since Django 2.0 the ForeignKey field requires the "on_delete" argument
    author = models.ForeignKey(User, on_delete=models.PROTECT, related_name='blog_posts')
    body = models.TextField()
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='published')

    class Meta:
        ordering = ('-publish',)

    def __str__(self):
        return self.title
 