from rest_framework.test import APITestCase, force_authenticate
from rest_framework.test import APIClient
from django.contrib.auth.models import User
import json

class BasicTests(APITestCase):
    def setUp(self):
        self.username = 'tsvetomir'
        self.password = 'openmarkets123'
        self.user = User.objects.create(username = self.username, password = self.password)
        self.client.force_authenticate(user = self.user)

    def test_root_api(self):
        response = self.client.get('/api/')
        self.assertEqual(response.status_code, 200)

    def test_create_bond(self):
        response = self.client.post('/api/bonds/', { "isin": "FR0000131104", "size": 100000000, "currency": "EUR", "maturity": "2025-02-28", "lei": "R0MUWSFPU8MPRO8K5P83" }, format='json')
        self.assertEqual(response.status_code, 201)

        response = self.client.get('/api/bonds/')
        convert = json.loads(response.content)
        legal_name = convert[0]['legal_name']
        self.assertEqual(response.status_code, 200)
        self.assertEqual(legal_name, 'BNP PARIBAS')


class AdvancedTests(APITestCase):
    def setUp(self):
        self.username = 'tsvetomir'
        self.password = 'openmarkets123'
        self.user = User.objects.create(username = self.username, password = self.password)
        self.client.force_authenticate(user = self.user)

        response = self.client.post('/api/bonds/', { "isin": "FR0000131104", "size": 100000000, "currency": "EUR", "maturity": "2025-02-28", "lei": "R0MUWSFPU8MPRO8K5P83" }, format='json')
        self.assertEqual(response.status_code, 201)

    def test_get_bonds(self):
        response = self.client.get('/api/bonds/')
        self.assertEqual(response.status_code, 200)

    def test_get_bond_legalName(self):
        response = self.client.get('/api/bonds/?legal_name=BNP PARIBAS')
        convert = json.loads(response.content)
        legal_name = convert[0]['legal_name']

        self.assertEqual(response.status_code, 200)
        self.assertEqual(legal_name, 'BNP PARIBAS')

    def test_get_bond_egalName_conditional(self):
        response = self.client.get('/api/bonds/?legal_name=BNP')
        convert = json.loads(response.content)
        legal_name = convert[0]['legal_name']

        self.assertEqual(response.status_code, 200)
        self.assertEqual(legal_name, 'BNP PARIBAS')

    def test_get_bond_isin(self):
        response = self.client.get('/api/bonds/?isin=FR0000131104')
        convert = json.loads(response.content)
        legal_name = convert[0]['legal_name']

        self.assertEqual(response.status_code, 200)
        self.assertEqual(legal_name, 'BNP PARIBAS')

    def test_get_bond_currency(self):
        response = self.client.get('/api/bonds/?currency=EUR')
        convert = json.loads(response.content)
        legal_name = convert[0]['legal_name']

        self.assertEqual(response.status_code, 200)
        self.assertEqual(legal_name, 'BNP PARIBAS')

    def test_get_bond_currency_conditional(self):
        response = self.client.get('/api/bonds/?currency=eu')
        convert = json.loads(response.content)
        legal_name = convert[0]['legal_name']

        self.assertEqual(response.status_code, 200)
        self.assertEqual(legal_name, 'BNP PARIBAS')
