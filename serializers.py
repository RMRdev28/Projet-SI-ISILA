from rest_framework import serializers
from .models import Utilisateur, Centre, Employe, Fournisseur, Client, Achat, Vente, Produit, Transfert, Versement, MasAbs, Login


class ProduitSerializer(serializers.ModelSerializer):

    class Meta:
        model = Produit
        fields = "__all__"