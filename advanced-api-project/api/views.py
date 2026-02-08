from django.shortcuts import render

# Create your views here.
from rest_framework import generics, permissions
from .models import Book
from .serializers import BookSerializer


class BookListView(generics.ListAPIView):
    """
    GET: List all books (public).
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.AllowAny]


class BookDetailView(generics.RetrieveAPIView):
    """
    GET: Retrieve a single book by ID (public).
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.AllowAny]


class BookCreateView(generics.CreateAPIView):
    """
    POST: Create a new book (authenticated users only).
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]


class BookUpdateView(generics.UpdateAPIView):
    """
    PUT/PATCH: Update an existing book (authenticated users only).
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]


class BookDeleteView(generics.DestroyAPIView):
    """
    DELETE: Remove a book (authenticated users only).
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]
