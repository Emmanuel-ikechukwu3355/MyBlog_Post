# from django import forms
# from .models import Post, Comment

# class PostForm(forms.ModelForm):
#     class Meta:
#         model = Post
#         fields = ["author", "title", "content"]

# class CommentForm(forms.ModelForm):
#     class Meta:
#         model = Comment
#         fields = ["name", "email", "body"]


    # name = forms.CharField(max_length=100, label="Your Name")
    # email = forms.EmailField(label="Your Email")
    # message = forms.CharField(
    #     widget=forms.Textarea(attrs={"rows": 5, "placeholder": "Write your feedback..."}),
    #     label="Your Feedback"
    # )


from django import forms
from .models import Post


# Form for creating or editing a blog post
class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content']
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter post title...',
            }),
            'content': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Write your post content here...',
                'rows': 6,
            }),
        }


# Optional: Form for adding comments
class CommentForm(forms.Form):
    name = forms.CharField(
        max_length=80,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Your name'})
    )
    body = forms.CharField(
        widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Add a comment...'})
    )
