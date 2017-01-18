from pprint import pprint
import json

from django.test import TestCase
from django.test import Client

from models import Counter

from utils.logger_test import LogTestCase
from utils.handlers import StreamMockHandler


class HTTPOpsTest(TestCase):

    def test_get_home_response(self):
        client = Client()
        response = client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_get_counter_response(self):
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

class LogsCaptureTest(LogTestCase):

    def test_get_home_logs(self):
        client = Client()
        with self.assertLogs('dl_logger', level='INFO') as cm:
            response = client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(cm.output), 1)

class LogsAddHandlerTest(LogTestCase):

    def test_get_home_logs(self):
        client = Client()
        StreamMockHandler.reset()
        with self.assertLogs('dl_logger', level='INFO') as cm:
            response = client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(cm.output), 1)
        print('added stream_handler captured this record')
        for rec in StreamMockHandler.get_records():
            pprint(rec)
            self.assertIsNotNone(rec['request'])
            self.assertEqual(rec['request']['path'], '/')
            self.assertIsNotNone(rec['response'])
            self.assertEqual(rec['response']['status'], 200)
