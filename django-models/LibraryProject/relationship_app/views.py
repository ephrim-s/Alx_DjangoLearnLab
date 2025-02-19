from django.shortcuts import render
from django.http import HttpResponse
from .models import Library, Author, Book, Librarian
from django.views.generic import ListView
from django.views.generic.detail import DetailView

def list_books(request):
    books = Book.objects.all()
    return render(request, 'relationship_app/list_books.html', {"books": books})

class BookListView(ListView):
    model = Book
    template_name = 'relationship_app/library_detail.html'
    context_object_name = "library"

class LibraryDetailView(DetailView):
    model = Library
    template_name = "library_detail.html"  
    context_object_name = "library" 