from django.shortcuts import render
from django.core.paginator import Paginator
from blog.models import Post
from django.db.models import Q

PER_PAGE = 9

def index(request):
    # posts = Post.objects \
    #     .filter(is_published=True) \
    #     .order_by('-pk')
    posts = Post.objects.get_published()
    paginator = Paginator(posts, PER_PAGE)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'page_obj': page_obj
    }
    return render(
        request,
        'blog/pages/index.html',
        context
    )

def created_by(request, author_id):
    # posts = Post.objects \
    #     .filter(is_published=True) \
    #     .order_by('-pk')
    posts = Post.objects.get_published() \
        .filter(created_by__pk=author_id)
    
    paginator = Paginator(posts, PER_PAGE)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'page_obj': page_obj
    }
    return render(
        request,
        'blog/pages/index.html',
        context
    )

def category(request, category_slug):
    # posts = Post.objects \
    #     .filter(is_published=True) \
    #     .order_by('-pk')
    posts = Post.objects.get_published() \
        .filter(category__slug=category_slug)

    paginator = Paginator(posts, PER_PAGE)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'page_obj': page_obj
    }
    return render(
        request,
        'blog/pages/index.html',
        context
    )

def tag(request, tag_slug):
    # posts = Post.objects \
    #     .filter(is_published=True) \
    #     .order_by('-pk')
    posts = Post.objects.get_published() \
        .filter(tags__slug=tag_slug)

    paginator = Paginator(posts, PER_PAGE)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'page_obj': page_obj
    }
    return render(
        request,
        'blog/pages/index.html',
        context
    )

def post(request, slug):
    post = Post.objects.get_published() \
        .filter(slug=slug) \
        .first()
    
    context = {
        'post': post
    }
    return render(
        request,
        'blog/pages/post.html',
        context
    )

def page(request):
    context = {
        'site': 'site'
    }
    return render(
        request,
        'blog/pages/page.html',
        context
    )
        
def search(request):

    search_value = request.GET.get('search', '').strip()

    posts = Post.objects.get_published() \
        .filter(
            Q(title__icontains=search_value) |
            Q(excerpt__icontains=search_value) |
            Q(content__icontains=search_value)
        )[:PER_PAGE]
    
    context = {
        'page_obj': posts,
        'search_value': search_value
    }
    return render(
        request,
        'blog/pages/index.html',
        context
    )