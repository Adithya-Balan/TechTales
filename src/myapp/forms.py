from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import blogs, comments

class ResgisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ["first_name", "last_name", "username", "email", "password1", "password2"]

        
class TechBlogForm(forms.ModelForm):
    class Meta:
        model = blogs
        fields = ['title', 'image', 'content']
        
        widgets ={
            'title': forms.TextInput(attrs={'size': 50, 'style': 'width:30%;'}),
            'content': forms.Textarea(attrs={'rows': 30, 'cols': 90})
        }
        
        
class CommentForm(forms.ModelForm):
    
    class Meta:
        model = comments
        fields = ['content']
        labels = {
            'content': "Add your Comment",
        }
        widgets = {
            'content': forms.Textarea(attrs={'rows': 10, 'cols': 61})
        }
