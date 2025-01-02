from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    # Put the "new article" path BEFORE the article detail path
    path('article/new/', views.article_create, name='article_create'),
    # Other specific article paths should also come before the detail view
    path('article/<slug:slug>/edit/', views.article_edit, name='article_edit'),
    path('article/<slug:slug>/delete/', views.article_delete, name='article_delete'),
    # Put the article detail path LAST
    path('article/<slug:slug>/', views.article_detail, name='article_detail'),
    path('dashboard/', views.dashboard, name='dashboard'),
]