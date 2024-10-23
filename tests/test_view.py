from django.test import TestCase, Client
from django.urls import reverse
from home.models import Place
from account.models import CustomUser
from home.forms import ContactForm
from account.forms import CustomAuthenticationForm
from django.contrib.messages import get_messages


class HomeViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        Place.objects.create(
            name="Test Place",
            phone=1234567890,
            description='A wonderful place to visit.',
            address='869 Test St, Test City',
            rate=4,
            city='Test City',
            image='path/to/image.jpg',
            location='50.1234, -1.2345',
            location_type='Park')

    def test_home_view_status_code(self):
        response = self.client.get(reverse('home:home'))
        self.assertEqual(response.status_code, 200)

    def test_home_view_template(self):
        response = self.client.get(reverse('home:home'))
        self.assertTemplateUsed(response, 'home/index.html')

    def test_home_view_context(self):
        response = self.client.get(reverse('home:home'))
        self.assertIn('city', response.context)
        self.assertIn('types', response.context)


class ContactViewTest(TestCase):
    def setUp(self):
        self.client = Client()

    def test_contact_view_status_code(self):
        response = self.client.get(reverse('home:contact'))
        self.assertEqual(response.status_code, 200)

    def test_contact_view_template(self):
        response = self.client.get(reverse('home:contact'))
        self.assertTemplateUsed(response, 'home/contact.html')

    def test_contact_view_post(self):
        response = self.client.post(reverse('home:contact'), {'name': 'Test', 'email': 'test@example.com', 'message': 'Test message', 'subject': 'Test subject'})
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('home:contact'))




class AboutViewTest(TestCase):
    def setUp(self):
        self.client = Client()

    def test_about_view_status_code(self):
        response = self.client.get(reverse('home:about'))
        self.assertEqual(response.status_code, 200)

    def test_about_view_template(self):
        response = self.client.get(reverse('home:about'))
        self.assertTemplateUsed(response, 'home/about.html')



class PlacesViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.place = Place.objects.create(
            name="Test Place",
            phone=1234567890,
            description='A wonderful place to visit.',
            address='869 Test St, Test City',
            rate=4,
            city='Test City',
            image='path/to/image.jpg',
            location='50.1234, -1.2345',
            location_type='Park')

    def test_places_view_status_code(self):
        response = self.client.get(reverse('home:places', args=[1]))
        self.assertEqual(response.status_code, 200)

    def test_places_view_template(self):
        response = self.client.get(reverse('home:places', args=[1]))
        self.assertTemplateUsed(response, 'list.html')


class SignUpViewTest(TestCase):
    def setUp(self):
        self.client = Client()

    def test_signup_view_get_status_code(self):
        response = self.client.get(reverse('account:signup'))
        self.assertEqual(response.status_code, 200)

    def test_signup_view_template(self):
        response = self.client.get(reverse('account:signup'))
        self.assertTemplateUsed(response, 'account/register2.html')

    def test_signup_view_post(self):
        response = self.client.post(reverse('account:signup'), {
            'username': 'testuser',
            'email': 'test@example.com',
            'full_name': 'Test User',
            'password1': 'alireza5698',
            'password2': 'alireza5698'
        })
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('home:home'))


class CustomLoginViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = CustomUser.objects.create_user(username='testuser', email='test@example.com', full_name='Test User', password='password123')

    def test_login_view_get_status_code(self):
        response = self.client.get(reverse('account:login'))
        self.assertEqual(response.status_code, 200)

    def test_login_view_template(self):
        response = self.client.get(reverse('account:login'))
        self.assertTemplateUsed(response, 'account/login2.html')

    def test_login_view_post(self):
        response = self.client.post(reverse('account:login'), {
            'username': 'testuser',
            'password': 'password123'
        })
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('home:home'))


class LogoutViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = CustomUser.objects.create_user(username='testuser', email='test@example.com', full_name='Test User', password='password123')
        self.client.login(username='testuser', password='password123')

    def test_logout_view(self):
        response = self.client.get(reverse('account:logout'))
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('home:home'))


class ProfileViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = CustomUser.objects.create_user(username='testuser', email='test@example.com', full_name='Test User', password='password123')
        self.client.login(username='testuser', password='password123')

    def test_profile_view_status_code(self):
        response = self.client.get(reverse('account:profile'))
        self.assertEqual(response.status_code, 200)

    def test_profile_view_template(self):
        response = self.client.get(reverse('account:profile'))
        self.assertTemplateUsed(response, 'account/profile.html')

    def test_profile_view_context(self):
        response = self.client.get(reverse('account:profile'))
        self.assertIn('profile', response.context)
        self.assertIn('photo', response.context)


class PlaceListTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.place = Place.objects.create(
            name="Test Place",
            phone=1234567890,
            description='A wonderful place to visit.',
            address='869 Test St, Test City',
            rate=4,
            city='Test City',
            image='path/to/image.jpg',
            location='50.1234, -1.2345',
            location_type='Park')

    def test_place_list_view_status_code(self):
        response = self.client.get(reverse('api:list'))
        self.assertEqual(response.status_code, 200)

    def test_place_list_view_content(self):
        response = self.client.get(reverse('api:list'))
        self.assertEqual(len(response.json()), Place.objects.count())


class PlaceDetailTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.place = Place.objects.create(
            name="Test Place",
            phone=1234567890,
            description='A wonderful place to visit.',
            address='869 Test St, Test City',
            rate=4,
            city='Test City',
            image='path/to/image.jpg',
            location='50.1234, -1.2345',
            location_type='Park')

    def test_place_detail_view_status_code(self):
        response = self.client.get(reverse('api:detail', args=[self.place.id]))
        self.assertEqual(response.status_code, 200)

    def test_place_detail_view_content(self):
        response = self.client.get(reverse('api:detail', args=[self.place.id]))
        self.assertEqual(response.json()['name'], self.place.name)


class UserListTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = CustomUser.objects.create_user(username='testuser', email='test@example.com', full_name='Test User', password='password123')

    def test_user_list_view_status_code(self):
        response = self.client.get(reverse('api:user-list'))
        self.assertEqual(response.status_code, 200)

    def test_user_list_view_content(self):
        response = self.client.get(reverse('api:user-list'))
        self.assertEqual(len(response.json()), CustomUser.objects.count())


class UserDetailTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = CustomUser.objects.create_user(username='testuser', email='test@example.com', full_name='Test User', password='password123')

    def test_user_detail_view_status_code(self):
        response = self.client.get(reverse('api:user-detail', args=[self.user.id]))
        self.assertEqual(response.status_code, 200)

    def test_user_detail_view_content(self):
        response = self.client.get(reverse('api:user-detail', args=[self.user.id]))
        self.assertEqual(response.json()['username'], self.user.username)
