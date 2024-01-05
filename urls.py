from django.urls import path
from . import views

urlpatterns = [
    path('produits/', views.get_all_products),
    path('utilisateurs/', views.get_all_users),
    path('emps/', views.get_all_emps),
    path('fournisseurs/', views.get_all_fournisseurs),
    path('clients/', views.get_all_clients),
    path('centres/', views.get_all_centres),
    
]