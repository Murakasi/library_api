from django.urls import path
from library import views

urlpatterns = [
    path("authors/", views.authors, name="authors"),
    path("authors/<int:pk>/", views.author_detail, name="detail"),
]
