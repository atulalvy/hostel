from django.http import HttpResponse
from django.shortcuts import render

from login.models import ApplicationSettings


def homepage(request):
    settings = ApplicationSettings.objects.get(pk=1)
    context =  {
        'show_allotment': settings.show_allotment
    }
    return render(request, 'Homepage/homepage.html',context)


def details(request):
    return render(request, 'Homepage/details.html')


def instructions(request):
    return render(request, 'Homepage/instructions.html')