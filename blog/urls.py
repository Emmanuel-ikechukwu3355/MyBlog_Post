from django.urls import path

from . import views

from blog.views import post_list

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path("feedback/", views.feedback_view, name="feedback"),
    path("thank-you/", views.thank_you, name="thank_you"),
]

# from . import views

# urlpatterns = [
#     path('', views.post_list, name='post_list'),
# ]