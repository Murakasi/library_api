from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from library.models import Author, Book

class AuthorSerializer(serializers.ModelSerializer):
    name = serializers.CharField(
        validators=[UniqueValidator(queryset=Author.objects.all())]
        )
    class Meta:
        model = Author
        fields = "__all__"


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
        fields = ["id", "title", "author", "author_id", "published_date", "pages"]
