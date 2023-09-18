from django.urls import path
# from django.contrib.auth.views import LogoutView

from accounts.views import (
    LoginView, UserCreateView,logout_view
)

app_name = 'accounts'

urlpatterns = [
    path("login/", LoginView.as_view(), name="login"),
    path("logout/", logout_view, name="logout"),
    path("sign-up/", UserCreateView.as_view(), name="sign_up"),
]
