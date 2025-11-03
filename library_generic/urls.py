from django.urls import path
from .views import AuthorListCreatView, AuthorRetrieveUpdateDestroyView, BookListCreateView, BookRetrieveUpdateDestroyView


urlpatterns = [
    path("authors/", AuthorListCreatView.as_view(), name="author_generic"),
    path("authors/<int:pk>", AuthorRetrieveUpdateDestroyView.as_view(), name="author_generic_detail"),
    path("books/", BookListCreateView.as_view(), name="books_generics"),
    path("books/<int:pk>", BookRetrieveUpdateDestroyView.as_view(), name="book_generic_detail"),
]
