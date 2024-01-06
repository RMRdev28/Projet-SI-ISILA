from django.db import models

# Create your models here.
class Centre(models.Model):
    desigC = models.CharField(max_length = 50,null=False)
    trashC = models.SmallIntegerField(default = 0)
    def __str__(self):
        return self.desigC
    
class Utilisateur(models.Model):
    TYPEUSER = (
    ('admin', 'Admin'),
    ('client', 'Client'),
    ('fournisseur', 'Fournisseur'),
    ('employe', 'Employe'),
    )   
    nom = models.CharField(max_length = 50,null=False)
    prenom = models.CharField(max_length = 50,null=False)
    adresse = models.CharField(max_length = 50,null=False)
    ville = models.CharField(max_length = 50,null=False)
    zipCode = models.CharField(max_length = 50,null=False)
    typeUtilisateur = models.CharField(max_length = 20, choices=TYPEUSER,default='client',null=False)
    trashU = models.SmallIntegerField(default = 0)
    def __str__(self):
        return self.nom+"-"+self.prenom
    
class Login(models.Model):
    userName = models.CharField(max_length = 50,null=False)
    Password = models.CharField(max_length = 250,null=False)
    def __str__(self):
        return self.userName

class Employe(models.Model):
    employe = models.ForeignKey(Utilisateur, on_delete = models.CASCADE, null=False)
    centre = models.ForeignKey(Centre, on_delete=models.CASCADE, null=False, related_name='employes')
    sallaire = models.FloatField()
    def calculer_salaire_mensuel(self, mois, annee):
        masabs_du_mois = self.masroufetabssences.filter(
            dateMA__year=annee, 
            dateMA__month=mois
        )

        total_masrouf = sum(masabs.montantMA for masabs in masabs_du_mois if masabs.typeMA == 'masrouf')
        jours_absence = masabs_du_mois.filter(typeMA='abssence').count()
        deduction_absence = jours_absence * self.sallaire
        salaire_final = (self.sallaire*30 - total_masrouf - deduction_absence)
        return salaire_final
    def __str__(self):
        return "Employe: "+self.employe.nom+'-'+self.employe.prenom+" Centre: "+self.centre.desigC

class Client(models.Model):
    client = models.ForeignKey(Utilisateur,on_delete = models.CASCADE, null=False)
    credit = models.FloatField(null=True, default=0)
    def __str__(self):
        return "Client: "+self.client.nom+'-'+self.client.prenom
        

class Fournisseur(models.Model):
    fournisseur = models.ForeignKey(Utilisateur,on_delete = models.CASCADE, null=False)
    solde = models.FloatField(null=True, default=0)
    def __str__(self):
        return "Fournisseur: "+self.fournisseur.nom+'-'+self.fournisseur.prenom

class Produit(models.Model):
    TYPEPRODUIT = (
        ('matiere','Matiere Premiere'),
        ('produit','Produit'),
    )
    desigP = models.CharField(max_length = 250,null=False)
    descP =  models.CharField(max_length = 250,null=False)
    typeP = models.CharField(max_length=10, choices=TYPEPRODUIT,default='matiere',null=False)
    qntEnStock = models.PositiveIntegerField()
    trashP = models.SmallIntegerField(default = 0)
    def __str__(self):
        return self.desigP
    def get_last_price(self):
        last_achat = Achat.objects.filter(prdA=self).order_by('-dateA').first()
        return last_achat.prixA if last_achat else 0


class Achat(models.Model):
    STATUTS = (
    ('incomplet', 'Incomplet'),
    ('complet', 'Complet'),
    )
    TYPEACHAT = (
        ('entièrement','Entièrement'),
        ('partiellement','Partiellement')
    )
    prdA = models.ForeignKey(Produit,on_delete=models.CASCADE, null=False)
    fournisseurA = models.ForeignKey(Fournisseur,on_delete = models.CASCADE, null=False)
    prixA = models.FloatField()
    qntA = models.PositiveIntegerField()
    dateA = models.DateTimeField(auto_now =True)
    typeA = models.CharField(max_length = 20, choices=TYPEACHAT,default='entièrement')
    statuA = models.CharField(max_length = 10, choices=STATUTS, default='incomplet')
    trashA = models.SmallIntegerField(default = 0)
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        produit = self.prdA
        produit.qntEnStock += self.qntA
        produit.save()
        if self.typeA == 'partiellement' and self.statuA == 'incomplet':
            fournisseur = self.fournisseurA
            fournisseur.solde += self.prixA*self.qntA
            fournisseur.save()

    def __str__(self):
        return "Achat : Produit: "+self.prdA.desigP
    


class Vente(models.Model):
    TYPEVENTES = (
        ('entièrement','Entièrement'),
        ('partiellement','Partiellement')
    )
    STATUTS = (
    ('incomplet', 'Incomplet'),
    ('complet', 'Complet'),
    )
    prdV = models.ForeignKey(Produit,on_delete=models.CASCADE, null=False)
    clientV = models.ForeignKey(Client,on_delete = models.CASCADE, null=False)
    prixV = models.FloatField()
    qntV = models.PositiveIntegerField()
    dateV = models.DateTimeField(auto_now =True)
    centre = models.ForeignKey(Centre, on_delete=models.CASCADE, null = True, related_name='ventes')
    statuV = models.CharField(max_length = 10, choices=STATUTS, default='incomplet') 
    typeV = models.CharField(max_length = 20, choices=TYPEVENTES,default='entièrement')
    trashV = models.SmallIntegerField(default = 0)
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        produit = self.prdV
        produit.qntEnStock -= self.qntV
        produit.save()
        if self.typeV == 'partiellement' and self.statuV == 'incomplet':
            client = self.clientV
            client.credit += self.prixV*self.qntV
            client.save()

    def __str__(self):
        return "Vente : Produit: "+self.prdV.desigP

class Versement(models.Model):
    dateVer = models.DateTimeField(auto_now=True)
    montantVer = models.FloatField()
    achat = models.ForeignKey(Achat, on_delete=models.CASCADE, related_name='versements', null=True, blank=True)
    vente = models.ForeignKey(Vente, on_delete=models.CASCADE, related_name='versements', null=True, blank=True)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        if self.achat:
            total_verse = sum([v.montantVer for v in self.achat.versements.all()])
            if total_verse >= self.achat.prixA*self.achat.qntA:
                self.achat.statuA = 'complet'
                self.achat.save()
            fournisseur = self.achat.fournisseurA
            fournisseur.solde -= self.montantVer
            fournisseur.save()

        elif self.vente:
            total_verse = sum([v.montantVer for v in self.vente.versements.all()])
            if total_verse >= self.vente.prixV:
                self.vente.statuV = 'complet'
                self.vente.save()
            client = self.vente.clientV
            client.credit -= self.montantVer
            client.save()

    def __str__(self):
        if self.achat:
            return "Versement pour achat: "+self.achat.prdA.desigP
        elif self.vente:
            return "Versement pour Vent: "+self.vente.prdV.desigP
            


class Transfert(models.Model):
    dateT = models.DateTimeField()
    prdT = models.ForeignKey(Produit,on_delete=models.CASCADE, null=False)
    qntT = models.PositiveIntegerField()
    totalT = models.FloatField(default = 0)
    centreT = models.ForeignKey(Centre, on_delete=models.CASCADE, null = True, related_name='transferts')
    def save(self, *args, **kwargs):
        self.totalT = self.prdT.get_last_price() * self.qntT
        super(Transfert, self).save(*args, **kwargs)

    def __str__(self):
        return "Transfer de : "+self.prdT.desigP+" A : "+self.centreT.desigC
    


class MasAbs(models.Model):
    TYPES = (
    ('abssence', 'Abssence'),
    ('masrouf', 'Masrouf'),
    )   
    dateMA = models.DateField()
    montantMA = models.FloatField(default = 0)
    typeMA = models.CharField(max_length = 10,choices = TYPES,default='abssence',null=False)
    empMA = models.ForeignKey(Employe, on_delete=models.CASCADE, null=False, related_name="masroufetabssences")
    def __str__(self):
        if self.typeMA == 'abssence':
            return "Abssence :"+self.empMA.employe.nom
        else:
            return "Masrouf :"+self.empMA.employe.nom
        



