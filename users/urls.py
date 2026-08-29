from django.urls import path
from .views import register, profile
from django.contrib.auth import views as auth_views

app_name = "users"


urlpatterns = [
    # add paths here
    path("login/", view=auth_views.LoginView.as_view(template_name="users/login.html"), name="login"),
    path("logout/", view=auth_views.LogoutView.as_view(template_name="users/logout.html"), name="logout"),

    path("register/", view=register, name="register"),
    path("profile/", view=profile, name="profile"),
]