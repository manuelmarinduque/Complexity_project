from django.urls import path
from . import views

# Create your urls here.

app_name = 'regions'

urlpatterns = [
    path('', views.homePage, name='home_page'),
]