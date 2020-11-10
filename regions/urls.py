from django.urls import path
from .views import HomePage, RegionCreateView, LinearProgrammingModel, ReinicioPage, RegionListView

# Create your urls here.

app_name = 'regions'

urlpatterns = [
    path('', HomePage.as_view(), name='home_page'),
    path('region_list/', RegionListView.as_view(), name='list_region_page'),
    path('region_create/', RegionCreateView.as_view(), name='create_region_page'),
    path('lp_model/', LinearProgrammingModel.as_view(), name='lp_model_page'),
    path('reiniciar', ReinicioPage.as_view(), name='reinicio_page'),
]