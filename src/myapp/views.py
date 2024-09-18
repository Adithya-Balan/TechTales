from django.shortcuts import redirect, render
from django.urls import reverse
from .forms import ResgisterForm, TechBlogForm, CommentForm
from .models import userinfo, comments, blogs
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login

#signals 
from django.db.models.signals import post_save


# Create your views here.
#Auth:
def sign_up(request):
    form = ResgisterForm()
    if request.method == "POST":
        print(True)
        form = ResgisterForm(request.POST)
        if form.is_valid():
            user_acc = form.save()
            print(True)
            login(request, user_acc) 
            return redirect('/home')
    context = {
        'form': form 
    }
    return render(request, 'registration/sign-up.html', context)

#signals for creating userinfo
def postsave_authuser(sender, instance, created, **kwargs):
    if created:
        print(instance)
        print(sender)
        userinfo.objects.create(user = instance)
        
post_save.connect(postsave_authuser,User)



#Business Logic
@login_required()
def home(request):
    user_obj = userinfo.objects.get(user = request.user)
    user_blog_obj = user_obj.user.blog_info.all()
    recent_blog= user_blog_obj.order_by('-id')[:3]
    context = {
        'user_obj': user_obj,
        'user_blog_obj': user_blog_obj,
        'recent_blog': recent_blog,
    }
    return render(request, 'myapp/index.html', context)

@login_required
def add_blog(request):
    form = TechBlogForm()
    if request.method == 'POST':
        form = TechBlogForm(request.POST, request.FILES)
        if form.is_valid():
            print(True)
            blog_obj = form.save(commit=False)
            blog_obj.user = request.user
            blog_obj.save()
            url = reverse('blog_page', args=[blog_obj.uuid])
            return redirect(url)
    context = {
        'form': form,

    }
    return render(request, 'myapp/add_blog.html', context)

@login_required
def blog_page(request, uuid_k):
    userinfo_obj = request.user.info
    blog_obj = blogs.objects.get(uuid = uuid_k)
    form = CommentForm()
    
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            form_obj = form.save(commit=False)
            form_obj.user = request.user
            form_obj.blog = blog_obj
            form_obj.save()
            url = reverse('blog_page', args=[blog_obj.uuid])
            return redirect(url)
        if 'uuid' in request.POST:
            if blog_obj in userinfo_obj.saved_post.all():
                print(True)
                userinfo_obj.saved_post.remove(blog_obj)
            else:
                print(False)
                userinfo_obj.saved_post.add(blog_obj)
            
    saved_posts = userinfo_obj.saved_post.all()
    comment_obj = comments.objects.filter(blog = blog_obj)
    comment_len = len(comment_obj)
    context = {
        'userinfo_obj': userinfo_obj,
        'blog_obj': blog_obj,
        'form': form,
        'comment_obj': comment_obj,
        'comment_len': comment_len,
        'saved_posts': saved_posts,
    }
    return render(request, 'myapp/blog_page.html', context)

@login_required
def your_blog(request):
    saved_obj = request.user.info.saved_post.all().order_by('-id')
    my_blogs = request.user.blog_info.all()
    print(my_blogs)
    print(saved_obj)
    context = {
        'saved_obj': saved_obj,
        'my_blogs': my_blogs,
    }
    return render(request, 'myapp/your_blog.html', context)

@login_required
def profile_page(request, id):
    user_obj = userinfo.objects.get(id = id)
    user_blog_obj = user_obj.user.blog_info.all()
    blog_len = len(user_blog_obj)
    print(blog_len)
    recent_blog= user_blog_obj.order_by('-id')[:3]
    print(recent_blog)
    
    
    context = {
        'user_obj': user_obj,
        'user_blog_obj': user_blog_obj,
        'recent_blog': recent_blog,
        'blog_len': blog_len,
    }
    return render(request, 'myapp/profile.html', context)