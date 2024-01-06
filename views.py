from django.shortcuts import render, get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Utilisateur, Centre, Employe, Fournisseur, Client, Achat, Vente, Produit, Transfert, Versement, MasAbs, Login
from .serializers import ProduitSerializer, UtilisateurSerializer, CentreSerializer, EmployeSerializer, ClientSerializer, FournisseurSerializer, AchatSerializer, VentesSerializer, VersementSerializer,TransferSerializer

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

@api_view(['GET'])
def get_all_achats(request):
    achats = Achat.objects.all()
    serializer = AchatSerializer(achats, many=True)  
    return Response({"achats": serializer.data})


@api_view(['GET'])
def get_all_ventes(request):
    ventes = Vente.objects.all()
    serializer = VentesSerializer(ventes, many=True)  
    return Response({"ventes": serializer.data})

@api_view(['GET'])
def get_versement_achat(request, id_achat):
    Versements = Versement.objects.filter(achat = id_achat)
    serializer = VersementSerializer(Versements, many=True)  
    return Response({"versements": serializer.data})

@api_view(['GET'])
def get_versement_vente(request, id_vente):
    Versements = Versement.objects.filter(vente = id_vente)
    serializer = VersementSerializer(Versements, many=True)  
    return Response({"versements": serializer.data})

@api_view(['GET'])
def get_transfer_center(request, id_centre):
    transferts = Transfert.objects.filter(centreT = id_centre)
    serializer = TransferSerializer(transferts, many=True)  
    return Response({"Transfers": serializer.data})

@api_view(['GET'])
def get_salaire_mois(request, id_emp, mois, anne):
    employe = get_object_or_404(Employe, pk=id_emp)
    salaire_mensuel = employe.calculer_salaire_mensuel(mois, anne)

    context = {"data":{
        'employe_id': employe.id,
        'employe_nom': f"{employe.employe.nom} {employe.employe.prenom}",
        'salaire_mensuel': salaire_mensuel,
        'mois': mois,
        'annee': anne
    }}
    return Response(context)


##inserting:



