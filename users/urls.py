from django.urls import path
from .views import register#, login, logout
from django.contrib.auth import views as auth_views

app_name = "users"


urlpatterns = [
    # add paths here
    path("", view=register, name="register"),
    path("login/", view=auth_views.LoginView.as_view(template_name="users/login.html"), name="login"),
    path("logout/", view=auth_views.LogoutView.as_view(template_name="users/logout.html"), name="logout"),
]