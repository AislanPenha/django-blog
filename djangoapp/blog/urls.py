from django.urls import path
from blog import views

app_name = 'blog'

urlpatterns = [
    path('', views.index, name='index'),
    path('post/<slug:slug>/', views.post, name='post'),
    path('created_by/<int:author_id>/', views.created_by, name='created_by'),
    path('category/<slug:category_slug>/', views.category_by, name='category_by'),
]
