from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Utilisateur, Centre, Employe, Fournisseur, Client, Achat, Vente, Produit, Transfert, Versement, MasAbs, Login
from .serializers import ProduitSerializer, UtilisateurSerializer, CentreSerializer, EmployeSerializer, ClientSerializer, FournisseurSerializer

# Create your views here.

#listing

@api_view(['GET'])
def get_all_products(request):
    products = Produit.objects.all()
    serializer = ProduitSerializer(products, many=True)  
    return Response({"produits": serializer.data})

@api_view(['GET'])
def get_all_users(request):
    users = Utilisateur.objects.all()
    serializer = UtilisateurSerializer(users, many=True)  
    return Response({"utilisateurs": serializer.data})

@api_view(['GET'])
def get_all_emps(request):
    emps = Employe.objects.all()
    serializer = EmployeSerializer(emps, many=True)  
    return Response({"employes": serializer.data})

@api_view(['GET'])
def get_all_clients(request):
    clients = Client.objects.all()
    serializer = ClientSerializer(clients, many=True)  
    return Response({"clients": serializer.data})

@api_view(['GET'])
def get_all_fournisseurs(request):
    fournisseurs = Fournisseur.objects.all()
    serializer = FournisseurSerializer(fournisseurs, many=True)  
    return Response({"fournisseurs": serializer.data})

@api_view(['GET'])
def get_all_centres(request):
    centres = Centre.objects.all()
    serializer = CentreSerializer(centres, many=True)  
    return Response({"centres": serializer.data})

