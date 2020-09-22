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
    informacion = [[50, 1000, 2, 5000000, 550, 0], 
                [25, 100, 4, 4000000, 350, 4], 
                [90, 3000, 1, 4000000, 2600, 0],
                [40, 500, 1, 1500000, 1000, 0],
                [35, 700, 1, 5000000, 300, 2],
                [22, 80, 3, 3500000, 250, 0],
                [30, 60, 2, 4500000, 300, 3]]
    objeto = LinearProgramming(num_regiones=7)
    tabla = objeto.construirTabla(informacion)
    tabla_modelo = objeto.generarTabla(tabla)
    valores_regiones, maximo_valor = objeto.modelo(tabla_modelo, 1000, 2000, 3500000000, 1000)
    distribucionVentiladores, distribucionProfesionales, distribucionPresupuesto, distribucionCualificacion = objeto.distribucionElementos(valores_regiones, tabla_modelo)
    return render(request, 'regions/home.html', {
        'distribucionVentiladores':distribucionVentiladores,
        'distribucionProfesionales':distribucionProfesionales,
        'distribucionPresupuesto':distribucionPresupuesto,
        'distribucionCualificacion':distribucionCualificacion,
        })
