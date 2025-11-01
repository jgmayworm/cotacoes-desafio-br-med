from django.urls import path
from . import views

urlpatterns = [
    path('taxas/', views.get_taxas),
]