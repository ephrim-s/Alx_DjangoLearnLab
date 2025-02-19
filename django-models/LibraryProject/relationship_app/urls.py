from django.urls import path
from . import views
from .views import list_books, LibraryDetailView

urlpatterns = [
    path('books/', views.all_books, name="books"),
    path('booklist/', views.BookListView.as_view(), name='library'),
]