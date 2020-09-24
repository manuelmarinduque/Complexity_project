from django.urls import path
from . import views

# Create your urls here.

app_name = 'regions'

urlpatterns = [
    path('', views.homePage, name='home_page'),
    path('regions/', views.modelPage, name='model_page'),
    path('regions/reiniciar', views.reinicioPage, name='reinicio_page'),
]