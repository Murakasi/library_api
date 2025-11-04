from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import AuthorViewSets, BookViewSets

router = DefaultRouter()
router.register(r"authors", AuthorViewSets, basename="authors")
router.register(r"books", BookViewSets, basename="books")
urlpatterns =[]

urlpatterns += router.urls

