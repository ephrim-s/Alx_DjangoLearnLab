from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Library, Author, Book, Librarian
from django.views.generic import ListView
from django.views.generic.detail import DetailView

def list_books(request):
    books = Book.objects.all()
    template = loader.get_template("relationship_app/list_books.html")
    context = {"books": books}
    return HttpResponse(template.render(context, request))

class BookListView(ListView):
    model = Book
    template_name = 'relationship_app/library_detail.html'
    context_object_name = "library"

class LibraryDetailView(DetailView):
    model = Library
    template_name = "library_detail.html"
    context_object_name = "library"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["books"] = self.object.book_set.all()  # Assuming a ForeignKey from Book to Library
        return context