from django.test import TestCase
from django.contrib.auth import get_user_model

class ModelTests(TestCase):
    """Test suites for ModelTests"""
    
    def test_create_user_with_email_successful(self):
        '''Test for creating a new user with an email'''
        email = "test@test.com"
        password = "Hello123"

        user = get_user_model().objects.create_user(
            email=email,
            password=password
            )
        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normalized(self):
        '''Test the email for a new user is normalized'''
        email = "test@TEST.COM"
        user = get_user_model().objects.create_user(email, 'test123')

        self.assertEqual(user.email, email.lower())

    def test_new_user_invalid_email(self):
        ''' Test to raise error if not email address is given'''
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None, 'test123')

    def test_create_new_superuser(self):
        ''''Test creating a new superuser'''
        user = get_user_model().objects.create_superuser(
            'test@test.com',
            'test123'
        )

        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)