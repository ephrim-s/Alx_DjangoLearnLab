from django.urls import path
from .views import BookList

urlpatterns = [
    path('api/', BookList.as_view(), name='book-list'),
]