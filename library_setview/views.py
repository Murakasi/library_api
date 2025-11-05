from django.shortcuts import render
from library.models import Author, Book
from library.serializers import AuthorSerializer, BookSerializer
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter

# Create your views here.

class AuthorViewSets(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    permission_classes = [IsAuthenticated]
    
    
    
class BookViewSets(viewsets.ModelViewSet):
    queryset = Book.objects.select_related("author").all()
    serializer_class = BookSerializer
    filter_backends = [ SearchFilter]
    # filterset_fields = ["title", "author"]
    search_fields = ["title", "author__name"]