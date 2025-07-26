from .models import Post, Category
from django.shortcuts import render, get_object_or_404, redirect
from .forms import CommentForm

def post_list_view(request):
    posts = Post.objects.filter(status=Post.Status.PUBLISHED).order_by('-published_at')
    context = {
        'posts': posts
    }
    return render(request, 'posts/post_list.html', context)

def post_detail_view(request, slug):
    post = get_object_or_404(Post, slug=slug)

    session_key = f'viewed_post_{post.id}'
    if not request.session.get(session_key, False):
        post.views += 1
        post.save(update_fields=['views'])
        request.session[session_key] = True

    comments = post.comments.all()
    comments_count = post.comments.count()
    if comments_count == 0:
        comments_count = 'Izohlar mavjud emas'
    else:
        comments_count = f"{comments_count} ta izoh"

    new_comment = None
    if request.method == "POST":
        form = CommentForm(data=request.POST)
        if form.is_valid():
            new_comment = form.save(commit=False)
            new_comment.post = post
            new_comment.user = request.user
            new_comment.save()
            return redirect('post_detail', slug=post.slug)
    else:
        form = CommentForm()
    context = {
        'post': post,
        'comments': comments,
        'comments_count': comments_count,
        'new_comment': new_comment,
        'form': form
    }
    return render(request, 'posts/post_detail.html', context)

def category_post_list_view(request, slug):
    category = get_object_or_404(Category, slug=slug)
    posts = Post.objects.filter(category=category, status=Post.Status.PUBLISHED).order_by('-published_at')
    context = {
        'category': category,
        'posts': posts
    }
    return render(request, 'posts/category_post_list.html', context)