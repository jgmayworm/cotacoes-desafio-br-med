from django.urls import path, include
from . import views

urlpatterns = [
    path('cotacoes/', views.get_taxas, name='get_taxas'),
]
