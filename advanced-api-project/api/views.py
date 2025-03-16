from django.shortcuts import render
from django_filters import FilterSet, CharFilter, NumberFilter
from rest_framework import generics
from rest_framework import OderingFilter
from rest_framework import DjangoFilterBackend
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from .serializers import BookSerializer
from .models import Book

class BookFilter(FilterSet):
    title = CharFilter(lookup_expr='icontains', label='Filter by title')
    author = CharFilter(lookup_expr='icontains', label='Filter by author')
    publication_year = NumberFilter(field_name='published_date__year', lookup_expr='exact', label='Filter by publication year')

    class Meta:
        model = Book
        fields = ['title', 'author', 'publication_year']


class BookListView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_class = [IsAuthenticatedOrReadOnly]
    filter_backends = (DjangoFilterBackend, OderingFilter)
    filterset_class = BookFilter
    search_fields = ['title', 'author']
    ordering_fields = ['title', 'published_date']
    ordering = ['title']

class BookDetailView(generics.RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_class = [IsAuthenticatedOrReadOnly]

class BookCreateView(generics.CreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_class = [IsAuthenticatedOrReadOnly]

class BookUpdateView(generics.UpdateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_class = [IsAuthenticatedOrReadOnly]

class BookDeleteView(generics.DestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_class = [IsAuthenticatedOrReadOnly]



