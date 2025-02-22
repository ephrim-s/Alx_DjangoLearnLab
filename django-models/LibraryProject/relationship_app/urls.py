from django.urls import path
from .views import list_books, LibraryDetailView, LoginView, LogoutView
from . import views
from .admin_view import admin_dashboard
from .librarian_view import librarian_dashboard
from .member_view import member_dashboard

urlpatterns = [
    path('books/', list_books, name="books"),
    path("library/<int:pk>/", LibraryDetailView.as_view(), name="library_detail"),
    path("register/", views.register, name="register"),
    path('login/', LoginView.as_view(template_name='relationship_app/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='relationship_app/logout.html'), name='logout'),
    path('admin-dashboard/', admin_dashboard, name='admin_dashboard'),
    path('librarian-dashboard/', librarian_dashboard, name='librarian_dashboard'),
    path('member-dashboard/', member_dashboard, name='member_dashboard'),
]