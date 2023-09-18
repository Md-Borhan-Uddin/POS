from django.urls import reverse_lazy
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin



class HomeView(LoginRequiredMixin ,TemplateView):
    template_name = "core/home.html"
    login_url = reverse_lazy('accounts:login')
    

    def get_queryset(self):
        return super().get_queryset()
    
