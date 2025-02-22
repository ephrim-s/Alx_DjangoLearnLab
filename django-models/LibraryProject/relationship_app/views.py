from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.views import LogoutView, LoginView
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import Library, Book
from django.views.generic.detail import DetailView
from django.contrib.auth.decorators import login_required, user_passes_test


def list_books(request):
    books = Book.objects.all()
    # template = loader.get_template("relationship_app/list_books.html")
    context = {"books": books}
    return render(request, 'relationship_app/list_books.html', context)

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

class LoginView(LoginView):
    template_name = 'relationship_app/login.html'

class LogoutView(LogoutView):
    template_name = 'relationship_app/logout.html'

def Admin(user):
    return hasattr(user, 'userprofile') and user.userprofile.role == 'Admin'

@user_passes_test(Admin)
def admin_dashboard(request):
    return render(request, 'admin_dashboard.html', {'user': request.user})