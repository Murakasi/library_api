from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from library.models import Author, Book

class AuthorSerializer(serializers.ModelSerializer):
    name = serializers.CharField(
        validators=[UniqueValidator(queryset=Author.objects.all())]
        )
    books = serializers.StringRelatedField(many=True, read_only=True)
    class Meta:
        model = Author
        fields = ["id", "name", "birth_year", "books"]


class BookSerializer(serializers.ModelSerializer):
    title = serializers.CharField(
        validators=[UniqueValidator(queryset=Book.objects.all())]
    )
    author = AuthorSerializer(read_only=True)
    author_id = serializers.PrimaryKeyRelatedField(
        queryset=Author.objects.all(),
        source="author",
        write_only=True
    )

    class Meta:
        model = Book
        fields = [
            "id", 
            "title",
            "author", 
            "author_id",
            "published_date",
            "pages"
            ]
    def validate_pages(self, value):
        if value < 50:
            raise serializers.ValidationError("Book can't have less than50 pages")
        if value > 1200:
            raise serializers.ValidationError("Book can't have mode 1200 pages")
        return value
