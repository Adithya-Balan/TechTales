from django.urls import path
from . import views

urlpatterns = [
    #Auth
    path('sign-up/', views.sign_up, name = ''),
    
    path("home/", views.home, name=""),
    path("add-blog/", views.add_blog, name="add_blog"),
    path("your-blog/", views.your_blog, name="your_blog"),
    
    path('blog-page/<uuid:uuid_k>', views.blog_page, name='blog_page'),
    path('profile/<int:id>', views.profile_page, name = 'profile_page'),
]
