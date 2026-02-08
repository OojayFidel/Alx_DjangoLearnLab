from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from api.models import Author, Book


class BookAPITests(APITestCase):
    """
    Unit tests for Book API endpoints:
    - CRUD operations
    - Filtering, search, ordering
    - Permissions (public read, auth required for write)
    """

    def setUp(self):
        # Create user for authenticated requests
        self.user = User.objects.create_user(username="tester", password="password123")

        # Create sample author + books
        self.author1 = Author.objects.create(name="Chinua Achebe")
        self.author2 = Author.objects.create(name="Wole Soyinka")

        self.book1 = Book.objects.create(
            title="Things Fall Apart", publication_year=1958, author=self.author1
        )
        self.book2 = Book.objects.create(
            title="No Longer at Ease", publication_year=1960, author=self.author1
        )
        self.book3 = Book.objects.create(
            title="The Interpreters", publication_year=1965, author=self.author2
        )

        # URLs (match your api/urls.py patterns)
        self.list_url = "/api/books/"
        self.detail_url = f"/api/books/{self.book1.id}/"
        self.create_url = "/api/books/create/"
        self.update_url = f"/api/books/update/{self.book1.id}/"
        self.delete_url = f"/api/books/delete/{self.book1.id}/"

    # ---------- READ (PUBLIC) TESTS ----------
    def test_list_books_public(self):
        """Anyone can list books."""
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(len(response.data) >= 3)

    def test_retrieve_book_public(self):
        """Anyone can retrieve a book by id."""
        response = self.client.get(self.detail_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["id"], self.book1.id)

    # ---------- CREATE (AUTH REQUIRED) ----------
    def test_create_book_unauthenticated_fails(self):
        """Unauthenticated users cannot create."""
        payload = {
            "title": "New Book",
            "publication_year": 2000,
            "author": self.author1.id,
        }
        response = self.client.post(self.create_url, payload, format="json")
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_create_book_authenticated_succeeds(self):
        """Authenticated users can create."""
        self.client.login(username="tester", password="password123")

        payload = {
            "title": "New Book",
            "publication_year": 2000,
            "author": self.author1.id,
        }
        response = self.client.post(self.create_url, payload, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data["title"], "New Book")

        self.assertTrue(Book.objects.filter(title="New Book").exists())

    # ---------- UPDATE (AUTH REQUIRED) ----------
    def test_update_book_unauthenticated_fails(self):
        payload = {"title": "Updated Title"}
        response = self.client.patch(self.update_url, payload, format="json")
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_update_book_authenticated_succeeds(self):
        self.client.login(username="tester", password="password123")

        payload = {"title": "Updated Title"}
        response = self.client.patch(self.update_url, payload, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        self.book1.refresh_from_db()
        self.assertEqual(self.book1.title, "Updated Title")

    # ---------- DELETE (AUTH REQUIRED) ----------
    def test_delete_book_unauthenticated_fails(self):
        response = self.client.delete(self.delete_url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_delete_book_authenticated_succeeds(self):
        self.client.login(username="tester", password="password123")

        response = self.client.delete(self.delete_url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Book.objects.filter(id=self.book1.id).exists())

    # ---------- FILTERING / SEARCH / ORDERING ----------
    def test_filter_books_by_publication_year(self):
        response = self.client.get(self.list_url, {"publication_year": 1960})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]["publication_year"], 1960)

    def test_filter_books_by_author(self):
        response = self.client.get(self.list_url, {"author": self.author2.id})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]["author"], self.author2.id)

    def test_search_books_by_title(self):
        response = self.client.get(self.list_url, {"search": "Interpreters"})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertIn("Interpreters", response.data[0]["title"])

    def test_search_books_by_author_name(self):
        response = self.client.get(self.list_url, {"search": "Achebe"})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(len(response.data) >= 2)

    def test_order_books_by_publication_year(self):
        response = self.client.get(self.list_url, {"ordering": "publication_year"})
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        years = [item["publication_year"] for item in response.data]
        self.assertEqual(years, sorted(years))
