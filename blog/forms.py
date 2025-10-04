from django import forms
from .models import Feedback

class FeedbackForm(forms.Form):
    name = forms.CharField(max_length=100, label="Your Name")
    email = forms.EmailField(label="Your Email")
    message = forms.CharField(
        widget=forms.Textarea(attrs={"rows": 5, "placeholder": "Write your feedback..."}),
        label="Your Feedback"
    )