from django.test import TestCase, RequestFactory
from django.urls import reverse
from animals.views import index

class AnimalsURLSTestCase(TestCase):
    def setUp(self):
        self.factory = RequestFactory()

    def test_route_in_view_index(self):
        request = self.factory.get('/')
        with self.assertTemplateUsed('index.html'):
            response = index(request)
            self.assertEqual(response.status_code, 200)