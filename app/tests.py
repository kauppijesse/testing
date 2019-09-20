from django.test import TestCase

# Create your tests here.
import json

from django.test import Client
from django.test import TestCase

class sum_test(TestCase):

    def setUp(self):
        self.client = Client()

    def test_test(self):
        """Animals that can speak are correctly identified"""
        url = "/test"
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        j = json.loads(response.content)
        self.assertEqual(j["data"], 3)

        response = self.client.post(url)
        self.assertEqual(response.status_code, 200)
        j = json.loads(response.content)
        self.assertEqual(j["data"], 4)
