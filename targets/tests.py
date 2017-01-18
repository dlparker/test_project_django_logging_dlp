import json
from django.test import TestCase
from django.test import Client
from models import Counter

class HomeGetTest(TestCase):

    def test_good_home_response(self):
        client = Client()
        response = client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_good_counter_response(self):
        client = Client()
        try:
            db_counter = Counter.objects.get(name="main")
            db_counter.delete()
        except Counter.DoesNotExist:
            pass
        response = client.get('/counter/')
        self.assertEqual(response.status_code, 200)
        counter = response.context['counter']
        self.assertIsNotNone(counter)
        self.assertEqual(counter.value, 1)

    def test_counter_increment(self):
        client = Client()
        db_counter,c = Counter.objects.get_or_create(name="main")
        response = client.post('/counter/', {})
        res_counter = response.context['counter']
        self.assertEqual(res_counter.value, db_counter.value + 1)

    def test_get_counter_ajax(self):
        client = Client()
        db_counter,c = Counter.objects.get_or_create(name="main")
        response = client.get('/counter/ajax/')
        self.assertEqual(response.status_code, 200)
        res = json.loads(response.content)
        self.assertEqual(res['counter']['value'], db_counter.value)

    def test_incr_counter_ajax(self):
        client = Client()
        db_counter,c = Counter.objects.get_or_create(name="main")
        response = client.get('/counter/incr/ajax/')
        self.assertEqual(response.status_code, 200)
        res = json.loads(response.content)
        self.assertEqual(res['counter']['value'], db_counter.value + 1)
