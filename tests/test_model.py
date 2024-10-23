from django.test import TestCase
from django.core.exceptions import ValidationError
from home.models import Place, Comment, Contact
from account.models import CustomUser
from django.utils.timezone import now
from django.db import IntegrityError



class CustomUserTests(TestCase):
    def setUp(self):
        self.user_data = {
            'username': 'testuser',
            'email': 'testuser@example.com',
            'full_name': 'Test User',
            'password': 'password123'
        }
        self.superuser_data = {
            'username': 'admin',
            'email': 'admin@example.com',
            'full_name': 'Admin User',
            'password': 'adminpassword'
        }

    def test_create_user(self):
        user = CustomUser.objects.create_user(**self.user_data)
        self.assertEqual(user.email, 'testuser@example.com')
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)
        self.assertTrue(user.check_password('password123'))

    def test_create_superuser(self):
        superuser = CustomUser.objects.create_superuser(**self.superuser_data)
        self.assertEqual(superuser.email, 'admin@example.com')
        self.assertTrue(superuser.is_staff)
        self.assertTrue(superuser.is_superuser)
        self.assertTrue(superuser.check_password('adminpassword'))

    def test_create_user_without_email(self):
        with self.assertRaises(ValueError):
            CustomUser.objects.create_user(username='nouser', email='', full_name='No Email User', password='password123')



class PlaceTests(TestCase):
    def setUp(self):
        self.place_data = {
            'name': 'Test Place',
            'phone': 1234567890,
            'description': 'A wonderful place to visit.',
            'address': '123 Test St, Test City',
            'rate': 5,
            'city': 'Test City',
            'image': 'path/to/image.jpg',
            'location': '50.1234, -1.2345',
            'location_type': 'Park'
        }

    def test_create_place(self):
        place = Place.objects.create(**self.place_data)
        self.assertEqual(place.name, 'Test Place')
        self.assertEqual(place.rate, 5)

    def test_rate_constraint(self):
        self.place_data['rate'] = 6
        with self.assertRaises(IntegrityError):
            Place.objects.create(**self.place_data)



class CommentTests(TestCase):
    def setUp(self):
        self.place = Place.objects.create(
            name='Test Place',
            phone=1234567890,
            description='A wonderful place to visit.',
            address='123 Test St, Test City',
            rate=5,
            city='Test City',
            image='path/to/image.jpg',
            location='50.1234, -1.2345',
            location_type='Park'
        )
        self.comment_data = {
            'name': 'Test Commenter',
            'email': 'commenter@example.com',
            'message': 'This is a test comment.',
            'place': self.place,
            'active': True
        }

    def test_create_comment(self):
        comment = Comment.objects.create(**self.comment_data)
        self.assertEqual(comment.name, 'Test Commenter')
        self.assertEqual(comment.place, self.place)
        self.assertTrue(comment.active)


class ContactTests(TestCase):
    def setUp(self):
        self.contact_data = {
            'name': 'Contact Name',
            'email': 'contact@example.com',
            'message': 'This is a contact message.',
            'subject': 'Contact Subject'
        }

    def test_create_contact(self):
        contact = Contact.objects.create(**self.contact_data)
        self.assertEqual(contact.name, 'Contact Name')
        self.assertEqual(contact.subject, 'Contact Subject')

