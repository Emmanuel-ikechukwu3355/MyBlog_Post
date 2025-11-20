# from django.urls import path
# from . import views

# urlpatterns = [
#     path('', views.post_list, name='post_list'),  # list of all posts
#     path('post/<int:pk>/', views.post_detail, name='post_detail'),  # single post
#     path('post/new/', views.post_create, name='post_create'),  # create post
#     path('post/<int:pk>/edit/', views.post_update, name='post_update'),  # edit post
#     path('post/<int:pk>/delete/', views.post_delete, name='post_delete'),  # delete post
# ]


from django.urls import path
from .views import (
    PostListView, PostDetailView, PostCreateView, 
    PostUpdateView, PostDeleteView
)

urlpatterns = [
    path('', PostListView.as_view(), name='post_list'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post_detail'),
    path('post/new/', PostCreateView.as_view(), name='post_create'),
    path('post/<int:pk>/edit/', PostUpdateView.as_view(), name='post_update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post_delete'),
]
