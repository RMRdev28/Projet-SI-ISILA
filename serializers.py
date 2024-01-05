from rest_framework import serializers
from .models import Utilisateur, Centre, Employe, Fournisseur, Client, Achat, Vente, Produit, Transfert, Versement, MasAbs, Login

##Listing

class ProduitSerializer(serializers.ModelSerializer):

    class Meta:
        model = Produit
        fields = "__all__"


## User serializers
class UtilisateurSerializer(serializers.ModelSerializer):

    class Meta:
        model = Utilisateur
        fields = "__all__"

class EmployeSerializer(serializers.ModelSerializer):
    employe = UtilisateurSerializer(read_only=True)
    class Meta:
        model = Employe
        fields = "__all__"

class FournisseurSerializer(serializers.ModelSerializer):
    fournisseur = UtilisateurSerializer(read_only=True)
    class Meta:
        model = Fournisseur
        fields = "__all__"

class ClientSerializer(serializers.ModelSerializer):
    client = UtilisateurSerializer(read_only=True)
    class Meta:
        model = Client
        fields = "__all__"

class CentreSerializer(serializers.ModelSerializer):

    class Meta:
        model = Centre
        fields = "__all__"