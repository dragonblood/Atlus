from django.views.generic import TemplateView
from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render_to_response
import numpy as np
import warnings
import pickle

class IndexPageView(TemplateView):
    template_name = 'main/index.html'


class ChangeLanguageView(TemplateView):
    template_name = 'main/change_language.html'


def atlus(request):
    return render(request, 'main/Atlus.html')

def boomerang(request):
    return render(request, 'main/Boomerang.html')

def about(request):
    return render(request, 'main/About.html')

def contact(request):
    return render(request, 'main/Contact.html')

def portfolio(request):
    return render(request, 'main/Portfolio.html')