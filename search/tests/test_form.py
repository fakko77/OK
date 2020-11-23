from search.forms import SignUpForm
from django.test import TestCase, Client
from django.contrib.auth.models import User


class TestSearchForm(TestCase):
    """class for testing form serach"""
    def test_anonymous_search(self):
        """test for launch a search not connected """
        response = self.client.get('/search/?query=', follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'search/index.html')
        response = self.client.post('/search/?query=', follow=True)
        self.assertEqual(response.status_code, 200)

    def test_login_search(self):
        """test for launch a search connected """
        c = Client()
        self.user = User.objects.create_user(username='testuser', password='12345')
        c.force_login(self.user)
        response = c.get('/search/?query=', follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'search/search.html')


class LogInTest(TestCase):
    """class for testing form login"""
    def setUp(self):
        self.credentials = {
                'username': 'fakko',
                'password': 'ty'}
        User.objects.create_user(**self.credentials)

    def test_login_post(self):
        """form post """
        response = self.client.post('/search/connect/', self.credentials, follow=True)
        self.assertTrue(response.context['user'].is_active)


class SingTest(TestCase):
    """class for testing form sing up """
    def test_register_false(self):
        """test register false"""
        form_params = {'first_name': 'John',
                       'last_name': 'Doe',
                       'email': 'john@doe',
                       'password': 'a',
                       'password_confirm': 'a',
                       'g-recaptcha-response': 'PASSED'}
        form = SignUpForm(form_params)
        self.assertFalse(form.is_valid())

