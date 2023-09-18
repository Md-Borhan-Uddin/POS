from django.urls import path, include
from django.conf.urls.static import static
from pos.settings import base

urlpatterns = [
    path("__reload__/", include("django_browser_reload.urls")),
]+ static(base.STATIC_URL, document_root = base.STATIC_ROOT)