from django.test import TestCase
from django.contrib.auth import get_user_model
from core import models


class Modeltests(TestCase):



    def test_create_user_with_email_successful(self):
        """test creating a new user with an email is successful"""
        email = 'test@ottawaappdev.com'
        password = '1234567890'
        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normalized(self):
        """Test the email for a new user is normalized"""
        email = 'test@LONDONAPPDEV.com'
        user = get_user_model().objects.create_user(email, 'test123')

        self.assertEqual(user.email, email.lower())

    def test_new_user_invalid_email(self):
        """Test creating user with no email raises error"""
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None, 'test123')

    def test_new_superuser(self):
        """Test creating a new superuser"""
        user = get_user_model().objects.create_superuser(
            'test@londonappdev.com',
            'test123'
        )

        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)

    def sample_user(self='test@londonappdev.com', password='testpass'):
        """Create a sample user"""
        return get_user_model().objects.create_user(self, password)

    def test_tag_str(self):
        """Test the tag string representation"""
        tag = models.Tag.objects.create(
            user=self.sample_user(),
            name='Vegan'
        )

        self.assertEqual(str(tag), tag.name)
