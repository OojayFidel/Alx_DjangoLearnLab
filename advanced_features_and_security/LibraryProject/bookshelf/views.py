from django.shortcuts import render
from django.contrib.auth.decorators import permission_required

@permission_required("bookshelf.can_view", raise_exception=True)
def book_list(request):
    return render(request, "bookshelf/book_list.html")

@permission_required("bookshelf.can_create", raise_exception=True)
def create_book(request):
    return render(request, "bookshelf/create_book.html")

@permission_required("bookshelf.can_edit", raise_exception=True)
def edit_book(request, pk):
    return render(request, "bookshelf/edit_book.html")

@permission_required("bookshelf.can_delete", raise_exception=True)
def delete_book(request, pk):
    return render(request, "bookshelf/delete_book.html")


from django.shortcuts import render
from .forms import BookSearchForm
from .models import Book

def secure_book_search(request):
    """
    Uses Django Forms for input validation and Django ORM for parameterized queries.
    Prevents SQL injection by avoiding raw SQL and string formatting in queries.
    """
    results = None

    if request.method == "POST":
        form = BookSearchForm(request.POST)
        if form.is_valid():
            q = form.cleaned_data["query"]
            results = Book.objects.select_related("author").filter(title__icontains=q)
    else:
        form = BookSearchForm()

    return render(request, "bookshelf/book_search.html", {"form": form, "results": results})


