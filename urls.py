from django.urls import path
from . import views

urlpatterns = [
    path('produits/', views.get_all_products),
    
]