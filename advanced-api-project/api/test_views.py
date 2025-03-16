# api/test_views.py

from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User
from .models import Book

class BookAPITests(APITestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='password123')
        self.token = Token.objects.create(user=self.user)

        self.book1 = Book.objects.create(title='Test Book 1', author='Author 1', published_date='2020-01-01')
        self.book2 = Book.objects.create(title='Test Book 2', author='Author 2', published_date='2021-01-01')

        self.book_list_url = reverse('book-list') 
        self.book_detail_url = lambda pk: reverse('book-detail', args=[pk])

    def test_create_book_authenticated(self):
        data = {
            'title': 'New Book',
            'author': 'New Author',
            'published_date': '2022-01-01'
        }

        response = self.client.post(
            self.book_list_url,
            data,
            HTTP_AUTHORIZATION='Token ' + self.token.key
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), 3)

    def test_create_book_unauthenticated(self):
        data = {
            'title': 'New Book',
            'author': 'New Author',
            'published_date': '2022-01-01'
        }
        response = self.client.post(self.book_list_url, data)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_update_book_authenticated(self):
        data = {
            'title': 'Updated Book Title',
            'author': 'Updated Author',
            'published_date': '2022-01-01'
        }
        response = self.client.put(
            self.book_detail_url(self.book1.pk),
            data,
            HTTP_AUTHORIZATION='Token ' + self.token.key
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.book1.refresh_from_db()
        self.assertEqual(self.book1.title, 'Updated Book Title')

    def test_delete_book_authenticated(self):
        response = self.client.delete(
            self.book_detail_url(self.book1.pk),
            HTTP_AUTHORIZATION='Token ' + self.token.key
        )
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Book.objects.count(), 1)

    def test_get_book_list(self):
        response = self.client.get(self.book_list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)  

        response = self.client.get(self.book_list_url, {'search': 'Test Book 1'})
        self.assertEqual(len(response.data), 1)

        response = self.client.get(self.book_list_url, {'ordering': 'published_date'})
        self.assertEqual(response.data[0]['title'], 'Test Book 1')  

        response = self.client.get(self.book_list_url, {'title': 'Test Book 1'})
        self.assertEqual(len(response.data), 1)

    def test_get_book_detail(self):
        response = self.client.get(self.book_detail_url(self.book1.pk))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], 'Test Book 1')

    def test_permissions_for_update_delete(self):
        user_without_permissions = User.objects.create_user(username='testuser2', password='password123')
        token_without_permissions = Token.objects.create(user=user_without_permissions)

        data = {'title': 'Unauthorized Update'}
        response = self.client.put(
            self.book_detail_url(self.book1.pk),
            data,
            HTTP_AUTHORIZATION='Token ' + token_without_permissions.key
        )
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)


        response = self.client.delete(
            self.book_detail_url(self.book1.pk),
            HTTP_AUTHORIZATION='Token ' + token_without_permissions.key
        )
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
