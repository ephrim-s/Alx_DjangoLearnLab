from bookshelf.models import Book

book = Book.objects.get(title="1984")
book.title = "Nineteen Eighty-Four"
book.save()

book_update = Book.objects.get(id=book.id)
print(book_update.title)