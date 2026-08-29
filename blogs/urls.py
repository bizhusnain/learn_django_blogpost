from . import views
from django.urls import path


app_name = "blogs"

urlpatterns = [
    path('', view=views.home, name="home"),
    path('about/', view=views.about, name="about"),
]