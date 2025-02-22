from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.views import LogoutView, LoginView
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
# from django.http import HttpResponse
# from django.template import loader
from .models import Library, Book
# from django.views.generic import ListView
from django.views.generic.detail import DetailView

def list_books(request):
    books = Book.objects.all()
    # template = loader.get_template("relationship_app/list_books.html")
    context = {"books": books}
    return render(request, 'relationship_app/list_books.html', context)

# class BookListView(ListView):
#     model = Book
#     template_name = 'relationship_app/library_detail.html'
#     context_object_name = "library"

class LibraryDetailView(DetailView):
    model = Library
    template_name = "library_detail.html"
    context_object_name = "library"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["books"] = self.object.book_set.all()  # Assuming a ForeignKey from Book to Library
        return context

def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('books')
    else:
        form = UserCreationForm()
    return render(request, 'relationship_app/register.html', {'form':form})
