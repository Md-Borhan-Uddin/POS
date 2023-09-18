from typing import Any
from django.http import HttpRequest, HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth import views
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.views.generic import TemplateView, RedirectView
from django.contrib.auth import logout

from accounts.forms import LoginForm, CustomUserCreationForm
from .models import User
# Create your views here.


class LoginView(views.LoginView):
    template_name = 'accounts/login.html'
    form_class = LoginForm
    success_url = reverse_lazy('core:home') 

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect(self.success_url)
        return super().get(request, *args, **kwargs) 



def logout_view(request):
    logout(request)
    return redirect(reverse_lazy('accounts:login'))


    
    
    

class UserCreateView(CreateView):
    model = User
    template_name = "accounts/register.html"
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('home')  
