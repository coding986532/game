from django.test import TestCase, Client
from django.contrib.auth.models import User
import json
from security.views import apitokencheck
class ApiLogonTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.client = Client()

    def test_apilogon_success(self):
        data = {
            'user': 'testuser',
            'pw': 'testpassword'
        }
        response = self.client.post('/apilogon', json.dumps(data), content_type='application/json')
        print(response.content)
        response_data = json.loads(response.content)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response_data['status'], 'Good')
        self.assertIn('token', response_data)
        self.assertIn('apitoken', response_data['token'])
        self.assertIn('apitokensig', response_data['token'])
        self.assertIn('Privlages', response_data['token'])
    def test_sig_verify(self):
        data = {
            'user': 'testuser',
            'pw': 'testpassword'
        }
        response = self.client.post('/apilogon', json.dumps(data), content_type='application/json')
        print(response.content)
        response_data = json.loads(response.content)
        token = response_data.get("token")
        result = apitokencheck(token)
        self.assertEqual(True, result)