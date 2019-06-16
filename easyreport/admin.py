from django.contrib import admin
from .models import Client, Fournisseur, Contact, Affaire



class ClientAdmin(admin.ModelAdmin):

    fieldsets =[
    ('Entreprise', {'fields' : ['code','nom','etablissement']}),
    ('Siège', {'fields': ['adresse_siege_1', 'adresse_siege_2', 'cp_siege', 'commune_siege']}),
    ('Facturation', {'fields': ['adresse_fact_1', 'adresse_fact_2', 'cp_fact', 'commune_fact']})
    ]


class FournisseurAdmin(admin.ModelAdmin):

    fieldsets = [
    ('Fournisseur', {'fields' : ['code', 'nom', 'etablissement']}),
    ]

class ContactAdmin(admin.ModelAdmin):

    fieldsets = [
    ('Contact', {'fields' : ['nom', 'prenom', 'client']}),
    ('Coordonnées', {'fields' : ['email', 'telephone']})
    ]

class AffaireAdmin(admin.ModelAdmin):

    fieldsets = [
    ('Identification du chantier', {'fields' : ['code', 'nom', 'client']}),
    ('Adresse du chantier', {'fields' : ['adresse_1', 'adresse_2', 'cp', 'commune']}),
    ('Contacts pour envoi des rapports', {'fields': ['contact']})
    ]




admin.site.register(Client, ClientAdmin)
admin.site.register(Fournisseur, FournisseurAdmin)
admin.site.register(Contact, ContactAdmin)
admin.site.register(Affaire, AffaireAdmin)

# Register your models here.
