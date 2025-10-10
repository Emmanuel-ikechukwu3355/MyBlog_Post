from django import forms
from .models import Post, Comment

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ["author", "title", "content"]

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ["name", "email", "body"]


    # name = forms.CharField(max_length=100, label="Your Name")
    # email = forms.EmailField(label="Your Email")
    # message = forms.CharField(
    #     widget=forms.Textarea(attrs={"rows": 5, "placeholder": "Write your feedback..."}),
    #     label="Your Feedback"
    # )