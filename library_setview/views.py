from django.shortcuts import render
from library.models import Author, Book
from library.serializers import AuthorSerializer, BookSerializer
from rest_framework import viewsets

# Create your views here.

class AuthorViewSets(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    
    
class BookViewSets(viewsets.ModelViewSet):
    queryset = Book.objects.select_related("author").all()
    serializer_class = BookSerializer