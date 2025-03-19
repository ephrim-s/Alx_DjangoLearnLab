from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User

class BlogViewsTestCase(TestCase):
    def test_register_view(self):
        response = self.client.get(reverse('register'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'blog/register.html')

    def test_login_view(self):
        response = self.client.get(reverse('login'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'blog/login.html')

    def test_profile_view_requires_login(self):
        response = self.client.get(reverse('profile'))
        self.assertNotEqual(response.status_code, 200)  # Should redirect to login
