from django.urls import path

from . import views

urlpatterns = [
    path("", views.capture_image, name="index"),
]