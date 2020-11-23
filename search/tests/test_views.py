from django.test import TestCase, Client
from django.contrib.auth.models import User


class TestViews(TestCase):

    def test_view_index(self):
        """test for view index status and template"""
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'search/index.html')

    def test_view_login_page(self):
        """test for view login status and template"""
        response = self.client.get('/search/login/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'search/login.html')

    def test_view_legal_notice(self):
        """test for view legal status and template"""
        response = self.client.get('/search/legal/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'search/legal_notice.html')

    def test_account_info(self):
        """test for view account status and template"""
        c = Client()
        self.user = User.objects.create_user(username='testuser', password='12345')
        c.force_login(self.user)
        response = c.get('/search/account/', follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'search/account.html')

    def test_my_food_anonymous(self):
        """test food page render not connected """
        response = self.client.get('/search/my-foods/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'search/index.html')

    def test_my_food_login(self):
        """test for view food status and template"""
        c = Client()
        self.user = User.objects.create_user(username='testuser', password='12345')
        c.force_login(self.user)
        response = c.get('/search/my-foods/', follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'search/myfood.html')
