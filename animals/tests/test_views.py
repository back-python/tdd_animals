from urllib import response
from django.test import TestCase, RequestFactory
from django.db.models.query import QuerySet
from animals.models import Animal


class IndexViewTestCase(TestCase):
    def setUp(self):
        self.factory = RequestFactory()
        self.animal = Animal.objects.create(
            animal_name = 'Piton',
            venomous = False,
            predator = True,
            domestic = False
        )

    def test_index_view_return_animals_description(self):
        """ Teste que verifica se a index retorna as características do animal pesquisado """
        response = self.client.get('/',
            {'buscar':'Piton'}
        )
        animal_pesquisado = response.context['caracteristicas']
        self.assertIs(type(animal_pesquisado),QuerySet)
        self.assertEqual(animal_pesquisado[0].animal_name, 'Piton')