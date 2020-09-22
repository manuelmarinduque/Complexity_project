from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from .classes.generar_tabla import LinearProgramming

# Create your views here.


def homePage(request):
    if request.method == 'POST':
        numero_regiones = request.POST.get('num_regions')
        return HttpResponseRedirect(reverse('regions:model_page', args=(numero_regiones , )))
    else:
        return render(request, 'regions/home.html')

def modelPage(request, numero_regiones):
    objeto = LinearProgramming(num_regiones=7)
    tabla = objeto.construirTabla()
    tabla_modelo = objeto.generarTabla(tabla)
    valores_regiones, maximo_valor = objeto.modelo(tabla_modelo)
    distribucionVentiladores, distribucionProfesionales, distribucionPresupuesto, distribucionCualificacion = objeto.distribucionElementos(valores_regiones, tabla_modelo)
    return render(request, 'regions/home.html', {
        'distribucionVentiladores':distribucionVentiladores,
        'distribucionProfesionales':distribucionProfesionales,
        'distribucionPresupuesto':distribucionPresupuesto,
        'distribucionCualificacion':distribucionCualificacion,
        })
