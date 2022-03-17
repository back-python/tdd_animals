from django.test import TestCase, RequestFactory
from animals.models import Animal


class AnimalModelsTestCase(TestCase):
    def setUp(self):
        self.animal = Animal.objects.create(
            animal_name = 'Leão',
            venomous = False,
            predator = True,
            domestic = True
        )

    def test_animal_exists_in_db(self):
        self.assertEqual(self.animal.animal_name, 'Leão')
