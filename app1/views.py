from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.core.mail import send_mail
from . import models
from . import forms


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
    error = False
    if 'q' in request.GET and request.GET['q']:
        q = request.GET['q']
        degrees = models.Test.objects.filter(name__icontains=q)
        return render(request, 'result.html', {'degrees': degrees, 'q': q})
    else:
        error = True
        return render(request, 'search_form.html', {'error': error})


def contact_form(request):
    if request.method == 'POST':
        form = forms.Forms(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            send_mail(
                cd['subject'],
                cd['message'],
                cd.get('email', 'noreply@example.com'),
                ['siteowner@example.com'],
        )
            return HttpResponseRedirect('/contact/thanks/')
    else:
        form = forms.Forms(initial={'subject': 'Hi'})
    return render(request, 'form.html', {'form': form})