from django.views.generic import ListView, CreateView, RedirectView
from django.http import JsonResponse
from django.shortcuts import redirect
from django.urls import reverse_lazy
from .models import Region
from .forms import FormData, RegionForm
from .classes.generar_tabla import LinearProgramming


# Create your views here.

class HomePage(ListView):
    model = Region
    template_name = 'regions/home.html'
    context_object_name = 'regiones'
    extra_context = {'form': FormData, 'regionform': RegionForm}


class RegionCreateView(CreateView):
    model = Region
    form_class = RegionForm
    success_url = reverse_lazy('regions:home_page')

    # No se podrá acceder a esta vista si se conoce la url, porque en ese caso se redirecciona a home_page
    def get(self, request, *args, **kwargs):
        return redirect('regions:home_page')

    def form_valid(self, form):
        self.object = form.save()
        mensaje = f'{self.model.__name__} registrada correctamente!'
        return JsonResponse({'message': mensaje})

    def form_invalid(self, form):
        mensaje = f'La {self.model.__name__} no se ha podido registrar!'
        return JsonResponse({'message': mensaje, 'error': form.errors})

class LinearProgrammingModel(ListView):
    model = Region
    template_name = 'regions/home.html'
    context_object_name = 'regiones'
    extra_context = {'form': FormData, 'regionform': RegionForm}

    def get(self, request, *args, **kwargs):
        informacion = [[region.existing_population, region.current_personal, region.required_personal, region.generated_costs, region.deads, region.qualification] for region in self.get_queryset()]
        objeto = LinearProgramming(numero_regiones=len(informacion))
        tabla = objeto.construirTabla(informacion)
        tabla_modelo = objeto.generarTabla(tabla)
        valores_regiones, maximo_valor = objeto.modelo(tabla_modelo, request.GET)
        distribucionVentiladores, distribucionProfesionales, distribucionPresupuesto, distribucionCualificacion = objeto.distribucionElementos(valores_regiones, tabla_modelo)
        self.extra_context.update({
            'distribucionVentiladores':distribucionVentiladores,
            'distribucionProfesionales':distribucionProfesionales,
            'distribucionPresupuesto':distribucionPresupuesto,
            'distribucionCualificacion':distribucionCualificacion
            })
        return super().get(self, request, *args, **kwargs)

class ReinicioPage(RedirectView):
    url = reverse_lazy('regions:home_page')
    
    def post(self, request, *args, **kwargs):
        Region.objects.all().delete()
        return super().post(self, request, *args, **kwargs)
