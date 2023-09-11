from django.shortcuts import render
from .forms import CustomUserCreationForm
from django.views import generic
from django.urls import reverse_lazy


class SignUpView (generic.CreateView):
    form_class = CustomUserCreationForm
    template_name = "registration/signup.html"
    success_url = reverse_lazy("login")
