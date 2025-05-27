from rest_framework.test import APITestCase
from django.urls import reverse
from rest_framework import status
from bank.models import Client, Account

class ClientTests(APITestCase):

    # Test a Client without name
    def test_client_empty_name(self):
        data = {"client_name": " ", "client_mail": "test@test.com"}
        response = self.client.post(reverse('client-list'), data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    # Test a Client with an existing email
    def test_client_same_email(self):
        Client.objects.create(client_name="Raul", client_mail="raul@test.com")
        data = {"client_name": "Otro", "client_mail": "raul@test.com"}
        response = self.client.post(reverse('client-list'), data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    # Test a Client with an invalid email
    def test_client_invalid_email(self):
        data = {"client_name": "Raul", "client_mail": "invalid-email"}
        response = self.client.post(reverse('client-list'), data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn("client_mail", response.data)
    
    # Test to create a valid Client with a valid email
    def test_create_client_valid_email(self):
        data = {"client_name": "Ana", "client_mail": "ana@test.com"}
        response = self.client.post(reverse('client-list'), data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
    
    # Test to create an account with invalid number
    def test_create_invalid_account_number(self):
        
        client = Client.objects.create(client_name="Jose", client_mail="jose@test.com")

        data = {
            "client_mail": client.id,
            "account_number": "abc123"
        }
        response = self.client.post(reverse('account-list'), data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn("account_number", response.data)

    # Test to create an account with a valid number
    def test_create_account_number(self):

        client = Client.objects.create(client_name="Laura", client_mail="laura@test.com")

        data = {
            "client": client.id,
            "account_number": "12345678"
        }
        response = self.client.post(reverse('account-list'), data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
    





