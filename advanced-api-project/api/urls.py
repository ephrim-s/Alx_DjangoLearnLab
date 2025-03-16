from django.urls import path
from . import views

urlpatterns = [
    path("books/", views.BookListView.as_view(), name="book-list"),
    path("books/detail/<int:pk>/", views.BookDetailView.as_view(), name="book-details"),
    path("books/create/", views.BookCreateView.as_view(), name="create-book"),
    path("books/update/<int:pk>/", views.BookUpdateView.as_view(), name="update-book"),
    path("books/delete/<int:pk>/", views.BookDeleteView.as_view(), name="delete-book"),
]
