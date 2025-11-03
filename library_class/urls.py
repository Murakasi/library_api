from django.urls import path
from .views import AuthorListCreateView, AuthorRetrivePutDeleteView, BookListCreateView, BookRetriveUpdateDelete

urlpatterns = [
    path('author_class/', AuthorListCreateView.as_view(), name='author_claas'),
    path("author_class/<int:pk>", AuthorRetrivePutDeleteView.as_view(), name='author_detail'),
    path("book_class/", BookListCreateView.as_view(), name="book_class"),
    path("book_class/<int:pk>", BookRetriveUpdateDelete.as_view(), name="book_detail"),
]
