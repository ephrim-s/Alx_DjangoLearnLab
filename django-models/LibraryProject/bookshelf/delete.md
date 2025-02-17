from bookshelf.models import Book

book = Book.objects.get(title="Nineteen Eighty-four")
book.delete()
print(book deleted successfully)
