from django.urls import path
from .views import list_books, BookListView

urlpatterns = [
    path('books/', list_books, name="books"),
    path('booklist/', BookListView.as_view(), name='library'),
]