from accounts.forms import UserChangeForm
from accounts.models import User
from accounts.views import user_account_settings_view
from django.http import HttpRequest
from django.test import TestCase
from django.urls import reverse


class TestViewResponses(TestCase):
    def setUp(self):
        """Create a instance for testing"""
        self.user = User.objects.create(
            email="admin@admin.com", username="admin", password="Aa12Bb34", is_active=True
        )

    def test_user_account_settings_view(self):
        """Test case for new account registration"""
        request = HttpRequest()
        request.user = self.user
        response = user_account_settings_view(request)
        self.assertEqual(response.status_code, 200)
        self.assertIn(self.user.email, response.content.decode("utf-8"))
        request.method = "POST"
        request.POST = {"email": "editadmin@admin.com", "username": "admin"}
        response = user_account_settings_view(request)
        self.assertEqual(response.status_code, 302)
        self.assertEqual(self.user.email, "editadmin@admin.com")

    def test_register_view(self):
        """Test case for new account registration"""
        data = {
            "email": "user@admin.com",
            "username": "user",
            "password1": "12user34",
            "password2": "12user34",
        }
        url = reverse("register")
        post_response = self.client.post(url, data=data)
        self.assertEqual(post_response.status_code, 302)
        self.assertRedirects(post_response, "/login/")
        self.assertEqual(User.objects.count(), 2)
        # test registration page get response
        get_response = self.client.get(url)
        self.assertEqual(get_response.status_code, 200)

    def test_login_view(self):
        """Test case for login user"""
        data = {"email": "admin@admin.com", "password": "Aa12Bb34"}
        url = reverse("login")
        post_response = self.client.post(url, data=data)
        self.assertRedirects(post_response, "/")

    def test_logout_view(self):
        """Test case for logout user"""
        url = reverse("logout")
        response = self.client.get(url)
        self.assertRedirects(response, "/login/")
