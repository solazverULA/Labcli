from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect


from django.shortcuts import render
from django.views.generic import TemplateView


def home(request):
    return render(request, 'home.html')

def examenes(request):
    return render(request, 'examenes.html')

def servicios(request):
    return render(request, 'services.html')
# Create your views here.
