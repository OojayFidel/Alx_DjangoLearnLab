from django.shortcuts import render

# Set up a view that uses the serializer to retrieve and return book data.

from rest_framework import generics
from .models import Book
from .serializers import BookSerializer

class BookList(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
# In api/views.py, extend the existing view setup by adding a new class BookViewSet that handles all CRUD operations.
# Use rest_framework.viewsets.ModelViewSet, which provides implementations for various actions like list, create, retrieve, update, and destroy.

from rest_framework import viewsets

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

