from django.shortcuts import render
from django.db import models
from django.http import HttpResponse


def test(request):
    return HttpResponse('Hi!')
