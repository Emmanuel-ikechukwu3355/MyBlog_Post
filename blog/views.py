# from django.shortcuts import render, get_object_or_404, redirect
# from .models import Post
# from .forms import PostForm, CommentForm


# # 🟢 1. Display list of all posts
# def post_list(request):
#     posts = Post.objects.all()
#     return render(request, "blog/post_list.html", {"posts": posts})


# # 🟢 2. View details of a single post + its comments + add comment form
# def post_detail(request, pk):
#     post = get_object_or_404(Post, pk=pk)
#     comments = post.comments.all()  # get all comments linked to this post

#     if request.method == "POST":
#         comment_form = CommentForm(request.POST)
#         if comment_form.is_valid():
#             comment = comment_form.save(commit=False)
#             comment.post = post  # link comment to the current post
#             comment.save()
#             return redirect("post_detail", pk=post.pk)
#     else:
#         comment_form = CommentForm()

#     return render(
#         request,
#         "blog/post_detail.html",
#         {"post": post, "comments": comments, "comment_form": comment_form},
#     )


# # 🟢 3. Create a new post
# def post_create(request):
#     if request.method == "POST":
#         form = PostForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect("post_list")
#     else:
#         form = PostForm()
#     return render(request, "blog/post_form.html", {"form": form})


# # 🟢 4. Update an existing post
# def post_update(request, pk):
#     post = get_object_or_404(Post, pk=pk)
#     if request.method == "POST":
#         form = PostForm(request.POST, instance=post)
#         if form.is_valid():
#             form.save()
#             return redirect("post_detail", pk=post.pk)
#     else:
#         form = PostForm(instance=post)
#     return render(request, "blog/post_form.html", {"form": form})


# # 🟢 5. Delete a post
# def post_delete(request, pk):
#     post = get_object_or_404(Post, pk=pk)
#     if request.method == "POST":
#         post.delete()
#         return redirect("post_list")
#     return render(request, "blog/post_confirm_delete.html", {"post": post})



from django.urls import reverse_lazy, reverse
from django.views.generic import (
    ListView, DetailView, CreateView, UpdateView, DeleteView
)
from django.shortcuts import redirect
from .models import Post
from .forms import PostForm, CommentForm


# ✅ LIST ALL POSTS
class PostListView(ListView):
    model = Post
    template_name = "blog/post_list.html"
    context_object_name = "posts"


# ✅ POST DETAILS + COMMENTS + COMMENT FORM
class PostDetailView(DetailView):
    model = Post
    template_name = "blog/post_detail.html"
    context_object_name = "post"

    # Add comments + form to context
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        post = self.get_object()
        context["comments"] = post.comments.all()
        context["comment_form"] = CommentForm()
        return context

    # Handle POST request for comment submission
    def post(self, request, *args, **kwargs):
        self.object = self.get_object()  # current post
        comment_form = CommentForm(request.POST)

        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.post = self.object
            comment.save()
            return redirect("post_detail", pk=self.object.pk)

        # if invalid, reload page with errors
        context = self.get_context_data(comment_form=comment_form)
        return self.render_to_response(context)
    

# ✅ CREATE NEW POST
class PostCreateView(CreateView):
    model = Post
    form_class = PostForm
    template_name = "blog/post_form.html"
    success_url = reverse_lazy("post_list")


# ✅ UPDATE POST
class PostUpdateView(UpdateView):
    model = Post
    form_class = PostForm
    template_name = "blog/post_form.html"

    def get_success_url(self):
        return reverse("post_detail", kwargs={"pk": self.object.pk})


# ✅ DELETE POST
class PostDeleteView(DeleteView):
    model = Post
    template_name = "blog/post_confirm_delete.html"
    success_url = reverse_lazy("post_list")
