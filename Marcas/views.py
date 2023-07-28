from django.shortcuts import render
from django.urls import reverse_lazy 
from django.http import HttpResponse
from django.template import loader
from django.views.generic import ListView
from django.views.generic import CreateView
from django.views.generic import UpdateView
from django.views.generic import DetailView
from django.views.generic import DeleteView
from Marcas.models import *
from Marcas.forms import *

# Create your views here.

def index(request):
    return render(request, 'index.html')

class CargarMarca(CreateView):
    model = Marcas
    fields = ['nombre', 'tipo', 'clase', 'fecha']
    success_url = reverse_lazy('index')

class CargarModelo(CreateView):
    model = ModelosIndustriales
    fields = ['nombre', 'clase', 'subclase', 'fecha']
    success_url = reverse_lazy('index')

class CargarDiseño(CreateView):
    model = DiseñosIndustriales
    fields = ['nombre', 'clase', 'subclase', 'fecha']
    success_url = reverse_lazy('index')

def busqueda(request):
    form = BuscarForm()
    if request.method == 'POST':
        form = BuscarForm(request.POST)
        if form.is_valid():
            nombre = form.cleaned_data['nombre']

            marcas = Marcas.objects.filter(nombre__icontains=nombre)
            diseños = DiseñosIndustriales.objects.filter(nombre__icontains=nombre)
            modelos = ModelosIndustriales.objects.filter(nombre__icontains=nombre)

            return render(request, 'Marcas/resultados_busqueda.html', {'marcas': marcas, 'modelos': modelos, 'diseños': diseños})
        else:
            form = BuscarForm()
    
    return render(request, 'Marcas/buscar.html', {'form': form})
