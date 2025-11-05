from django.urls import path
from library import views


urlpatterns = [
    path("authors/", views.authors, name="authors"),
    path("authors/<int:pk>/", views.author_detail, name="author_detail"),
    path("books/", views.books, name="books"),
    path("books/<int:pk>/", views.books_detail, name="book_detail"),
    path("secrets/", views.get_secret, name="secret"),
]
