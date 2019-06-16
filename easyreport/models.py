from django.db import models

# Create your models here.

class Client(models.Model):

    code = models.CharField("Code ID", max_length=10)
    nom = models.CharField("Nom", max_length=100)
    etablissement = models.CharField("Etablissement", blank=True, max_length=100)

    adresse_siege_1 = models.CharField('Adresse', max_length = 200)
    adresse_siege_2 = models.CharField("Complément", blank=True, max_length = 200)
    cp_siege = models.CharField("Code postal", max_length = 10)
    commune_siege = models.CharField("Commune", max_length = 100)

    adresse_fact_1 = models.CharField('Adresse', blank=True, max_length = 200)
    adresse_fact_2 = models.CharField("Complément", blank=True, max_length = 200)
    cp_fact = models.CharField("Code postal", blank=True, max_length = 10)
    commune_fact = models.CharField("Commune", blank=True, max_length = 100)

    def __str__(self):
        return self.code


class Contact(models.Model):

    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    nom = models.CharField('Nom', max_length=100)
    prenom = models.CharField('Prénom', max_length=100)
    email = models.EmailField('Adresse e-mail')
    telephone = models.CharField('Numéro de téléphone', blank=True, max_length = 15)

    def __str__(self):
        return self.nom

class Fournisseur(models.Model):

    code = models.CharField('Code ID', max_length = 15)
    nom = models.CharField('Nom', max_length = 100)
    etablissement = models.CharField('Etablissement', blank=True, max_length = 100)

    def __str__(self):
        return self.code

class Formule(models.Model):

    denomination = models.CharField('Dénomination', max_length = 100)
    fournisseur = models.ForeignKey(Fournisseur, on_delete=models.CASCADE)
    resistance = models.FloatField()

    def __str__(self):
        return self.denomination

class Affaire(models.Model):

    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    code = models.CharField("Code de l'affaire", max_length = 15)
    nom = models.CharField('Nom du chantier', max_length = 100)

    adresse_1 = models.CharField('Adresse', max_length = 200)
    adresse_2 = models.CharField("Complément", blank=True, max_length = 200)
    cp = models.CharField("Code postal", max_length = 10)
    commune = models.CharField("Commune", max_length = 100)

    contact = models.ManyToManyField(Contact)

    formule = models.ManyToManyField(Formule)

    def __str__(self):
        return self.code


class BonLivraison(models.Model):

    affaire = models.ForeignKey(Affaire, on_delete=models.CASCADE)
    formule = models.ForeignKey(Formule, on_delete=models.CASCADE)
    num = models.CharField("Numéro du BL", max_length = 25)
    date = models.DateField("Date d'émission du BL")

    def __str__(self):
        return self.num

    class Meta:
        verbose_name = "Bon de livraison"
        verbose_name_plural = "Bons de livraisons"


class Epreuve(models.Model):

    num_bl = models.ForeignKey(BonLivraison, on_delete=models.CASCADE, verbose_name = 'Numéro de BL')
    date = models.DateField("Date de l'épreuve")
    d1 = models.FloatField('Diamètre (1)')
    d2 = models.FloatField('Diamètre (2)')
    d3 = models.FloatField('Diamètre (3)')
    h = models.FloatField('Hauteur', default=None)
    rc1 = models.FloatField('Epreuve (1')
    rc2 = models.FloatField('Epreuve (2)')
    rc3 = models.FloatField('Epreuve (3)', default=None)

    def __str__(self):
        return self.id
