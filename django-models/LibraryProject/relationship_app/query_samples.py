from relationship_app.models import Author, Book, Library, Librarian

def author_book(author):
    author_name = Author.objects.filter(author=author).first()
    if author:
        return author.books.all()
    return "No books available"

def libriary_books(library_name):
    library = Library.objects.get(name=library_name).first()
    if library:
        return library.books.all()
    return "No books available"

def librarian_library(library_name):
    library = Library.objects.get(name=library_name).first()
    if library:
        return library.librarian
    return "No librarian available"