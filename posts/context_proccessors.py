from .models import Post, Category

def latest_post(request):
    latest_posts = Post.objects.filter(status=Post.Status.Published).order_by('-published_at')[:4]
    context = {
        'latest_posts': latest_posts
    }
    return context
def trending_post(request):
    trending_posts = Post.objects.filter(status=Post.Status.Published).order_by('-views')[:4]
    context = {
        'trending_posts': trending_posts
    }
    return context

def nav_categories(request):
    nav_categories = Category.objects.filter(id__in=[1, 3])
    context = {
        'nav_categories': nav_categories
    }
    return context

def categories(request):
    categories = Category.objects.all()
    context = {
        'categories': categories
    }
    return context