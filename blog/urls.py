# from django.urls import path

# from . import views

# from blog.views import post_list

# urlpatterns = [
#     path('', views.post_list, name='post_list'),
#     path("feedback/", views.feedback_view, name="feedback"),
#     path("thank-you/", views.thank_you, name="thank_you"),
# ]




# blog/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path("", views.post_list, name="post_list"),
    path("post/<int:pk>/", views.post_detail, name="post_detail"),
    path("post/new/", views.post_create, name="post_create"),
    path("post/<int:pk>/edit/", views.post_update, name="post_update"),
    path("post/<int:pk>/delete/", views.post_delete, name="post_delete"),
]

# from . import views

# urlpatterns = [
#     path('', views.post_list, name='post_list'),
# ]