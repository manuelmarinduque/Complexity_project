from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from .classes.generar_tabla import LinearProgramming
from .models import Region

# Create your views here.


def homePage(request):
    regiones = Region.objects.all()
    if request.method == 'POST':
        informacion = {
            'name': request.POST.get('name'),
            'poblacion': request.POST.get('poblacion'),
            'estaciones_actuales': request.POST.get('estaciones_actuales'),
            'personal_requerido': request.POST.get('personal_requerido'),
            'costos': request.POST.get('costos'),
            'muertes': request.POST.get('muertes'),
            'cualificacion': request.POST.get('cualificacion'),
        }
        region = Region(**informacion)
        region.save()
        return render(request, 'regions/home.html', {'regiones': regiones})
    else:
        return render(request, 'regions/home.html', {'regiones': regiones})

def modelPage(request):
    regiones = Region.objects.all()
    informacion = [[region.poblacion, region.estaciones_actuales, region.personal_requerido, region.costos, region.muertes, region.cualificacion] for region in regiones]
    objeto = LinearProgramming(numero_regiones=len(informacion))
    tabla = objeto.construirTabla(informacion)
    tabla_modelo = objeto.generarTabla(tabla)
    valores_regiones, maximo_valor = objeto.modelo(tabla_modelo, request.POST)
    distribucionVentiladores, distribucionProfesionales, distribucionPresupuesto, distribucionCualificacion = objeto.distribucionElementos(valores_regiones, tabla_modelo)
    return render(request, 'regions/home.html', {
        'distribucionVentiladores':distribucionVentiladores,
        'distribucionProfesionales':distribucionProfesionales,
        'distribucionPresupuesto':distribucionPresupuesto,
        'distribucionCualificacion':distribucionCualificacion,
        'regiones': regiones,
        })
