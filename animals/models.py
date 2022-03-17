from django.db import models

# Create your models here.
class Animal(models.Model):
    animal_name = models.CharField(max_length=100, unique=True)
    venomous = models.BooleanField()
    predator = models.BooleanField()
    domestic = models.BooleanField()

    def __str__(self):
        return self.animal_name