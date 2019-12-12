from django.views.generic import TemplateView
from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render_to_response
import numpy as np
import warnings
import pickle
#from django.conf.urls.static import static

class IndexPageView(TemplateView):
    template_name = 'main/index.html'

class ChangeLanguageView(TemplateView):
    template_name = 'main/change_language.html'

def about(request):
    return render(request, 'static/About.html')

def contact(request):
    return render(request, 'static/Contact.html')

def portfolio(request):
    return render(request, 'static/Portfolio.html')