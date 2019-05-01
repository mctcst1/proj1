from django.shortcuts import render
from django.http import HttpResponse
from . import models


def test(request):
    name = models.Test.objects.get(id=1)
    data = models.Test.objects.all()
    return render(request, 'index.html', {'name': name, 'degree': 3.5, 'data': data})


def meta(request):
    # l = request.META
    # return render(request, 'meta.html', {'meta': l})
    dic = {'one': 1, 'two': 2}
    return render(request, 'meta.html', {'meta': dic})


def display_meta(request):
    values = request.META.items()
    html = []
    for k, v in values:
        html.append('<tr><td>%s</td><td>%s</td></tr>' % (k, v))
    return HttpResponse('<table>%s </table>' % '\n'.join(html))


def search_form(request):
    return render(request, 'search_form.html')


def search(request):
    if 'q' in request.GET:
        message = 'You search for %s' % (request.GET['q'])
    else:
        message = 'You submitted an empty form.'
    return HttpResponse(message)