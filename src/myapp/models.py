from django.db import models
from django.contrib.auth.models import User
import uuid

# Create your models here.
class blogs(models.Model):
    uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_info')
    title = models.CharField(max_length=50)
    content = models.TextField()
    image = models.ImageField(upload_to='blog_image')    
    published = models.DateField(auto_now=False, auto_now_add=True)
    modified = models.DateField(auto_now=True, auto_now_add=False)
    
class userinfo(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='info')
    profile_pic = models.ImageField(upload_to='profile_pic', default='profile_pic/profile.jpg')
    about_yourself = models.TextField(max_length=100, default='Not Updated Yet...')
    saved_post = models.ManyToManyField(blogs, related_name='saved_post')

    
class comments(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments')
    blog = models.ForeignKey(blogs, on_delete=models.CASCADE, related_name='comments_info')
    content = models.TextField()
    date = models.DateField(auto_now=False, auto_now_add=True)
    

    

   