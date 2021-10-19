from django.urls import path

from exit import views

urlpatterns = [
    path("home/", views.exit_home),
]