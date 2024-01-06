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

class AchatSerializer(serializers.ModelSerializer):
    prdA = ProduitSerializer(read_only = True)
    fournisseurA = FournisseurSerializer(read_only = True)
    class Meta:
        model = Achat
        fields = "__all__"

class VentesSerializer(serializers.ModelSerializer):
    prdV = ProduitSerializer(read_only = True)
    cleintV = ClientSerializer(read_only = True)
    class Meta:
        model = Vente
        fields = "__all__"


class VersementSerializer(serializers.ModelSerializer):
    achat = AchatSerializer(read_only = True)
    vente = VentesSerializer(read_only= True)
    class Meta:
        model =Versement
        fields = "__all__"

class TransferSerializer(serializers.ModelSerializer):
    prdT = ProduitSerializer(read_only = True)
    centreT = CentreSerializer(read_only=True)
    
    class Meta:
        model =Transfert
        fields = "__all__"