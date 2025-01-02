from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.utils.text import slugify
from .models import Article
from .forms import ArticleForm

def home(request):
    articles = Article.objects.all()
    return render(request, 'blog/home.html', {'articles': articles})

def article_detail(request, slug):
    article = get_object_or_404(Article, slug=slug)
    return render(request, 'blog/article_detail.html', {'article': article})

@login_required
def dashboard(request):
    articles = Article.objects.filter(author=request.user)
    return render(request, 'blog/dashboard.html', {'articles': articles})

@login_required
def article_create(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            article = form.save(commit=False)
            article.author = request.user
            article.slug = slugify(article.title)
            article.save()
            return redirect('dashboard')
    else:
        form = ArticleForm()
    return render(request, 'blog/article_form.html', {'form': form, 'title': 'Create Article'})

@login_required
def article_edit(request, slug):
    article = get_object_or_404(Article, slug=slug, author=request.user)
    if request.method == 'POST':
        form = ArticleForm(request.POST, instance=article)
        if form.is_valid():
            article = form.save(commit=False)
            article.slug = slugify(article.title)
            article.save()
            return redirect('dashboard')
    else:
        form = ArticleForm(instance=article)
    return render(request, 'blog/article_form.html', {'form': form, 'title': 'Edit Article'})

@login_required
def article_delete(request, slug):
    article = get_object_or_404(Article, slug=slug, author=request.user)
    article.delete()
    return redirect('dashboard')