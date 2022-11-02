from accounts.models import User
from django.test import TestCase

# Create your tests here.


class TestUserModel(TestCase):
    def setUp(self):
        """Create  instances for testing"""
        self.user1 = User.objects.create(email="admin@admin.com", username="username")
        self.user2 = User.objects.create(email="user@admin.com", grade=7)

    def test_user_model_entery(self):
        user1 = self.user1
        self.assertEqual(str(user1), "admin@admin.com")

    def test_user_model_methods(self):
        """Test case for next_grade method"""
        user1 = self.user1
        user2 = self.user2
        user1.next_grade()
        user2.next_grade()
        self.assertEqual(user1.grade, 2)
        self.assertEqual(user2.grade, 7)
