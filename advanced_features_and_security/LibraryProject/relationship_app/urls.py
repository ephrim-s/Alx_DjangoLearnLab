from django.urls import path
from .views import list_books, LibraryDetailView, LoginView, LogoutView, add_book, edit_book, delete_book, member_view, admin_view, librarian_view
from . import views
# from .admin_view import Admin
# from .librarian_view import Librarian
# from .member_view import Member

urlpatterns = [
    path('books/', list_books, name="books"),
    path("library/<int:pk>/", LibraryDetailView.as_view(), name="library_detail"),
    path("register/", views.register, name="register"),
    path('login/', LoginView.as_view(template_name='relationship_app/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='relationship_app/logout.html'), name='logout'),
    path('add_book/', add_book, name='add_book'),
    path('edit_book/<int:book_id>/', edit_book, name='edit_book'),
    path('delete/<int:boo_id>/', delete_book, name='delete_book'),
    path('admin/', admin_view, name='admin_dashboard'),
    path('librarian/', librarian_view, name='librarian_dashboard'),
    path('member/', member_view, name='member_dashboard'),
]
