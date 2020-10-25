from django.urls import path
from .views import HomePage, modelPage, reinicioPage, homePage

# Create your urls here.

app_name = 'regions'

urlpatterns = [
    path('home/', homePage, name='home_page'),
    path('', HomePage.as_view(), name='home_page2'),
    path('regions/', modelPage, name='model_page'),
    path('regions/reiniciar', reinicioPage, name='reinicio_page'),
]