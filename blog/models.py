from django.db import models


class BlogPost(models.Model):
    author = models.CharField(max_length=100)
    title = models.CharField(max_length=200)
    content = models.TextField()

    def __str__(self):
        return self.title

class Feedback(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()

    def __str__(self):
        return f"Feedback from {self.name}"
    


# Create your models here.
