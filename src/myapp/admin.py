from django.contrib import admin
from .models import userinfo, comments, blogs

# Register your models here.
admin.site.register(userinfo)
admin.site.register(blogs)
admin.site.register(comments)
