from django.shortcuts import render
from animals.models import Animal


def index(request):
    context = {
        'caracteristicas' : None,
    }

    if 'buscar' in request.GET:
        animais = Animal.objects.all()
        animal_pesquisado = request.GET['buscar']
        caracteristicas = animais.filter(animal_name__icontains = animal_pesquisado)

        context = {
            'caracteristicas' : caracteristicas,
        }

    return render(request, 'index.html', context)