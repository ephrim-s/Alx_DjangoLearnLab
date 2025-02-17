Create a Book instance
Commands used:

from bookshelf.models import Book

book = Book.objects.create(title="1984", author="George Orewell", publication_year=1949)
print(book)

Expected outputs:
1984 by George Orewell (1949)


Retrieve the book you created
Commands used:

from bookshelf.models import Book

book = Book.objects.get(title="1984")
print(book.title, book.author, book.publication_year)

Expected outputs:
1984 George Orewell 1949


Update the title of the created book
Command used:

from bookshelf.models import Book
book = Book.objects.get(title="1984")
book.title = "Nineteen Eighty-Four"
book.save()

book_update = Book.objects.get(id=book.id)
print(book_update)

Expected outputs:
Nineteen Eighty-Four by George Orewell (1949)


Delete the book instance
Command used:
from bookshelf.models import Book

book = Book.objects.get(title="Nineteen Eighty-four")
book.delete()

books = Book.objects.all()

Expected outputs:

Traceback (most recent call last):
  File "<console>", line 1, in <module>
AttributeError: type object 'Book' has no attribute 'Objects'. Did you mean: 'objects'?