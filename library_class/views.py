from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from library.models import Author, Book
from library.serializers import AuthorSerializer, BookSerializer
from rest_framework.response import Response
from rest_framework import status

# Create your views here.


class AuthorListCreateView(APIView):
    def get(sel, request):
        author = Author.objects.all()
        serializer = AuthorSerializer(author, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request):
        serializer = AuthorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        

class AuthorRetrivePutDeleteView(APIView):
    def get_object(self, pk):
        return get_object_or_404(Author, pk=pk)
    
    
    def get(self, request, pk):
        book = self.get_object(pk)
        serializer = AuthorSerializer(book)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def put(self,request, pk):
        book = self.get_object(pk)
        serializer = AuthorSerializer(book, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response({"error": "Bad request"}, status=status.HTTP_400_BAD_REQUEST)
        
        
    def delete(self, requst, pk):
        book = self.get_object(pk)
        book.delete()
        return Response({"delete": f"author with id {pk} was delete"}, status=status.HTTP_204_NO_CONTENT)
    
    
    
class BookListCreateView(APIView):
     def get(selr, request):
         book = Book.objects.select_related("author").all()
         serializer = BookSerializer(book, many="True")
         return Response(serializer.data, status=status.HTTP_200_OK)
        
     def post(self, request):
        serializer = BookSerializer(data=request.data)
        if serializer.is_valid():
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
        
class BookRetriveUpdateDelete(APIView):
    def get_object(self, pk):
            return get_object_or_404(Book, pk=pk)
        
    def get(self, request, pk):
        book = self.get_object(pk)
        serializer = BookSerializer(book)
        return Response(serializer.data, status=status.HTTP_200_OK)
        
    def put(self, request, pk):
        book = self.get_object(pk)
        serializer = BookSerializer(book, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)
        
    def delete(self, request, pk):
        book = self.get_object(pk)
        book.delete()
        return Response({"delete": f"Book with ig {pk} was delete"})