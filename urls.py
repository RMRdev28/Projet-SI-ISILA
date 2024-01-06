from django.urls import path
from . import views

urlpatterns = [
    path('produits/', views.get_all_products),
    path('utilisateurs/', views.get_all_users),
    path('emps/', views.get_all_emps),
    path('fournisseurs/', views.get_all_fournisseurs),
    path('clients/', views.get_all_clients),
    path('centres/', views.get_all_centres),
    path('achats/', views.get_all_achats),
    path('ventes/', views.get_all_ventes),
    path('achat/versement/<int:id_achat>', views.get_versement_achat),
    path('vente/versement/<int:id_vente>', views.get_versement_vente),
    path('centre/transfert/<int:id_centre>', views.get_transfer_center),
    path('employer/sallair/<int:id_emp>/<int:mois>/<int:anne>', views.get_salaire_mois),


    
]