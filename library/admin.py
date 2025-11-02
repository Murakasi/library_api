from django.contrib import admin
from library.models import Author, Book

# Register your models here.

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "birth_year"]
    search_fields = ["name"]
    list_per_page = 20
    list_filter = ["birth_year"]
    
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = [
        "id", 
        "title", 
        "author", 
        "published_date", 
        "pages"
        ]