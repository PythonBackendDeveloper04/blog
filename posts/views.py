from django.db.models import Q
from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from django.views.generic import ListView

from .models import Post, Category
from .forms import CommentForm

def home_view(request):
    posts = Post.objects.filter(status=Post.Status.Published).order_by('-published_at')[:4]
    context = {
        'posts': posts
    }
    return render(request, 'posts/home.html', context)

def detail_view(request,post):
    post = get_object_or_404(Post, slug=post)

    # Session orqali ko'rishlar sonini oshirish
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
            return redirect('post_detail', post=post.slug)
    else:
        form = CommentForm()
    context = {
        'post': post,
        'comments': comments,
        'comments_count': comments_count,
        'new_comment': new_comment,
        'form': form
    }
    return render(request, 'posts/detail.html', context)

def category_view(request, category_id):
    category = Category.objects.get(id=category_id)
    posts = Post.objects.filter(category=category, status=Post.Status.Published).order_by('-published_at')

    context = {
        'category': category,
        'posts': posts
    }
    return render(request, 'posts/category.html', context)

from django.shortcuts import render, redirect
from .forms import ContactForm

def contact_view(request):
    form = ContactForm()
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('contact')  # yoki boshqa sahifaga yo'naltiring
    return render(request, 'posts/contact.html', {'form': form})

class SearchView(ListView):
    model = Post
    template_name = 'posts/search.html'
    context_object_name = 'posts'

    def get_queryset(self):
        query = self.request.GET.get('q')
        return Post.objects.filter(
            Q(title__icontains=query) | Q(body__icontains=query)
        )