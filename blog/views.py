from django.shortcuts import render
from django.utils import timezone
from .models import Post
from django.http import HttpResponse

# Create your views here.
# main page
def post_list(request):
    posts = Post.objects.all()
    return render(request, 'blog/index.html', {'articles':posts})

def article_page(request, article_id):
    #posts = Post.objects.filter(published_data__lte=timezone.now()).order_by('published_data')
    #return render(request, 'blog/post_list.html', {'posts':posts})
    #return render(request, 'blog/post_list.html', {'arg':'first arg'})
    #return HttpResponse("Hello World!")
    post = Post.objects.get(pk=article_id)
    return render(request, 'blog/article_page.html', {'article':post})


def edit_page(request, article_id):
    if str(article_id) == '0':
        return render(request, "blog/edit_page.html")
    post = Post.objects.get(pk=article_id)
    return render(request, "blog/edit_page.html", {'article':post})


def edit_action(request):
    title = request.POST.get('title', "TITLE")
    content = request.POST.get('content', "CONTENT")
    article_id = request.POST.get('article_id','0')
    if article_id == '0':
        Post.objects.create(title=title, content=content)
        posts = Post.objects.all()
        return render(request, 'blog/index.html', {'articles':posts})
    post = Post.objects.get(pk=article_id)
    post.title = title
    post.content = content
    post.save()
    return render(request, 'blog/article_page.html', {'article':post})

