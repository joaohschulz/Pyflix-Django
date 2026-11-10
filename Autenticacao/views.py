from django.shortcuts import render
from django.contrib.auth.views import LogoutView
from django.contrib.auth.views import LoginView as DjangoLoginView
from django.views.generic import CreateView
from django.urls import reverse_lazy
from .forms import RegisterForm

class RegisterView(CreateView):
    form_class = RegisterForm
    template_name = 'register.html'
    success_url = reverse_lazy('login')

class LoginView(DjangoLoginView):
    template_name = 'login.html'

class LogoutView(LogoutView):
    template_name = 'logout.html'
    







