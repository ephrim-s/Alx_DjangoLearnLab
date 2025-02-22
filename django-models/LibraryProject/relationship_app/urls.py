from django.urls import path
from .views import list_books, LibraryDetailView, LoginView, LogoutView
from . import views

urlpatterns = [
    path('books/', list_books, name="books"),
    path("library/<int:pk>/", LibraryDetailView.as_view(), name="library_detail"),
    path("register/", views.register, name="register"),
]