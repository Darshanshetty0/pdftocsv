from django.urls import path

from . import views

urlpatterns = [
    path("test", views.index, name="index"),
    path("", views.home, name="home"),
    path("upload", views.upload_file, name="upload_file")
]