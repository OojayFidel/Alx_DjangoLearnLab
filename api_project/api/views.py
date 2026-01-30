from django.shortcuts import render

# Set up a view that uses the serializer to retrieve and return book data.

from rest_framework.generics import ListAPIView
from .models import Book
from .serializers import BookSerializer

class BookList(ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
