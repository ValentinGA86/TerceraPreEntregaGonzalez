"""
URL configuration for TerceraPE project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from Marcas.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', index, name='index'),
    path('busqueda/', busqueda, name='realizar_busqueda'),
    path('cargar_marca', CargarMarca.as_view(), name="cargar_marcas"),
    path('cargar_modelo', CargarModelo.as_view(), name="cargar_modelo"),
    path('cargar_dis/', CargarDiseño.as_view(), name="cargar_dis")
]
