from bookshelf.models import Book

book = Book.objects.create(title="1984", author="George Orewell", publication_year=1949)
print(book)
