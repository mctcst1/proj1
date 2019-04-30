from django.shortcuts import render
from . import models


def test(request):
    name = models.Test.objects.get(id=1)
    return render(request, 'index.html', {'name': name, 'degree': 3.5})
