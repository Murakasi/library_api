from django.urls import path
from library import views

urlpatterns = [
    path("authors/", views.authors, name="authors"),
]
