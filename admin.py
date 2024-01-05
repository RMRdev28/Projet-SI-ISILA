from django.contrib import admin
from .models import Utilisateur, Centre, Employe, Fournisseur, Client, Achat, Vente, Produit, Transfert, Versement, MasAbs, Login
# Register your models here.

admin.site.register(Utilisateur)
admin.site.register(Centre)
admin.site.register(Employe)
admin.site.register(Fournisseur)
admin.site.register(Client)
admin.site.register(Achat)
admin.site.register(Vente)
admin.site.register(Produit)
admin.site.register(Transfert)
admin.site.register(Versement)
admin.site.register(MasAbs)
admin.site.register(Login)