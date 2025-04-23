from django.urls import path
from . import views

urlpatterns = [
    path("", views.blogg),
    path("example", views.example),
]
