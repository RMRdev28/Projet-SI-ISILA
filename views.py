from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Utilisateur, Centre, Employe, Fournisseur, Client, Achat, Vente, Produit, Transfert, Versement, MasAbs, Login
from .serializers import ProduitSerializer

# Create your views here.
@api_view(['GET'])
def get_all_products(request):
    products = Produit.objects.all()
    serializer = ProduitSerializer(products, many=True)  
    return Response({"products": serializer.data})
