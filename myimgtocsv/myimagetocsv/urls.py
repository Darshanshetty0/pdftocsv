from django.urls import path

from . import views

urlpatterns = [
    path("test", views.index, name="index"),
    path("", views.upload_file, name="upload"),
    path("upload", views.upload_file, name="upload_file")
]