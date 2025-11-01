from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
# Create your models here.

class Author(models.Model):
    name = models.CharField(max_length=120, unique=True)
    birth_year = models.IntegerField(validators=[MaxValueValidator(2005), MinValueValidator(1940)])
    
    def __str__(self):
        return self.name
    
    class Meta:
        db_table = 'authors'
        ordering = ["name"]
    
    
    
    
class Book(models.Model):
    title = models.CharField(max_length=150, unique=True)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name="books")
    published_date = models.DateField()
    page = models.SmallIntegerField(validators=[MinValueValidator(50), MaxValueValidator(1200)])
    
    def __str__(self):
        return self.title
    
    class Meta:
        db_table = "books"
        ordering = ['title', 'published_date']
    


    