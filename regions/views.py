from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

# Create your views here.


def homePage(request):
    if request.method == 'POST':
        numero_regiones = request.POST.get('num_regions')
        return render(request, 'regions/home.html', {'num_regions': numero_regiones})
    else:
        return render(request, 'regions/home.html')
