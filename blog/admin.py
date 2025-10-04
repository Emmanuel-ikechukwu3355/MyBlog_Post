from django.contrib import admin
from .models import BlogPost
from .models import Feedback

admin.site.register(Feedback)



admin.site.register(BlogPost)

# Register your models here.
