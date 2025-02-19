from relationship_app.models import Author, Book, Library, Librarian

def author_book(author_name):
    author= Author.objects.get(name=author_name)
    author.objects.filter(author=author)
    if author:
        return author.books.all()
    return "No books available"

def libriary_books(library_name):
    library = Library.objects.get(name=library_name).first()
    if library:
        return library.books.all()
    return "No books available"

def librarian_library(library_name):
    library = Library.objects.filter(name=library_name).first()
    if library:
        try:
            return Librarian.objects.get(library=library)
        except Librarian.DoesNotExist:
            return "Not available"
    return "Not available"