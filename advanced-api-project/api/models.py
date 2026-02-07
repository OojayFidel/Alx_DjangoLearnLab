from django.db import models

class Author(models.Model):
    """
    Author model stores the name of a writer.
    One Author can have many Books (one-to-many relationship).
    """
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Book(models.Model):
    """
    Book model stores book details and links each book to an Author.
    """
    title = models.CharField(max_length=255)
    publication_year = models.IntegerField()
    author = models.ForeignKey(
        Author,
        on_delete=models.CASCADE,
        related_name='books'  # This allows author.books.all()
    )

    def __str__(self):
        return f"{self.title} ({self.publication_year})"
