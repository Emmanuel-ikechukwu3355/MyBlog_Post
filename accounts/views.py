# from django.contrib import messages
# from django.contrib.auth import authenticate, login, logout
# from django.contrib.auth.decorators import login_required
# from django.contrib.auth.models import User
# from django import forms
# from django.shortcuts import render, redirect


# # --- Registration Form ---
# class CustomUserCreationForm(forms.ModelForm):
#     password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
#     password2 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput)
#     bio = forms.CharField(label='Bio', widget=forms.Textarea, required=False)

#     class Meta:
#         model = User
#         fields = ['username', 'email']

#     def clean_password2(self):
#         password1 = self.cleaned_data.get("password1")
#         password2 = self.cleaned_data.get("password2")
#         if password1 and password2 and password1 != password2:
#             raise forms.ValidationError("Passwords don’t match.")
#         return password2

#     def save(self, commit=True):
#         user = super().save(commit=False)
#         user.set_password(self.cleaned_data["password1"])
#         if commit:
#             user.save()
#         return user


# # --- Register View ---
# def register_view(request):
#     if request.method == 'POST':
#         form = CustomUserCreationForm(request.POST)
#         if form.is_valid():
#             form.save()
#             messages.success(request, 'Account created successfully! You can now log in.')
#             return redirect('login')
#     else:
#         form = CustomUserCreationForm()
#     return render(request, 'accounts/register.html', {'form': form})


# # --- Login View ---
# def login_view(request):
#     if request.method == 'POST':
#         username = request.POST['username']
#         password = request.POST['password']
#         user = authenticate(request, username=username, password=password)
#         if user is not None:
#             login(request, user)
#             messages.success(request, f'Welcome back, {user.username}!')
#             return redirect('post_list')
#         else:
#             messages.error(request, 'Invalid username or password.')
#     return render(request, 'accounts/login.html')


# # --- Logout View ---
# def logout_view(request):
#     logout(request)
#     messages.success(request, 'You have successfully logged out.')
#     return redirect('login')


# # --- Profile View (protected) 


# @login_required
# def profile_view(request):
#     return render(request, 'accounts/profile.html')


from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic import CreateView, TemplateView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import get_user_model

User = get_user_model()


# REGISTER VIEW
class RegisterView(CreateView):
    template_name = "accounts/register.html"
    form_class = UserCreationForm
    success_url = reverse_lazy("login")

    def form_valid(self, form):
        # Save the user
        response = super().form_valid(form)
        return response


# LOGIN VIEW
class UserLoginView(LoginView):
    template_name = "accounts/login.html"
    form_class = AuthenticationForm

    def get_success_url(self):
        return reverse_lazy("home")  # redirect after login


# LOGOUT VIEW
class UserLogoutView(LogoutView):
    next_page = reverse_lazy("login")


# PROFILE VIEW
class ProfileView(LoginRequiredMixin, TemplateView):
    template_name = "accounts/profile.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["user"] = self.request.user
        return context
