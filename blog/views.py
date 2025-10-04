from django.shortcuts import render, redirect

from .forms import FeedbackForm

from .models import BlogPost



def post_list(request):
    posts = BlogPost.objects.all()
    return render(request, 'blog/post_list.html', {'posts' : posts})


def feedback_view(request):
    if request.method == "POST":
        form = FeedbackForm(request.POST)
        if form.is_valid():

            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']

            print(name, email, message)

            return redirect("thank_you")
        else:
            form = FeedbackForm()
        return render(request, "blog/feedback.html", {"form": form})
        
def thank_you(request):

        return render(request, "blog/thank_you.html")



#             name = form.cleaned_data["name"]
#             email = form.cleaned_data["email"]
#             message = form.cleaned_data["messsage"]

#             print(f"Feedback received from {name} ({email}): {message}")

#             return redirect("thank_you")
#     else:
#         form = FeedbackForm()
#     return render(request, "blog/feedback.html", {"form": form})

# def thank_you(request):
#     return render(request, "blog/thank_you.html")

