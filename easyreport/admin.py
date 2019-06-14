from django.contrib import admin
from .models import Client, Fournisseur, Contact, Affaire



class ClientAdmin(admin.ModelAdmin):

    fieldsets =[
    ('Entreprise', {'fields' : ['code','nom','etablissement']}),
    ('Siège', {'fields': ['adresse_siege_1', 'adresse_siege_2', 'cp_siege', 'commune_siege']}),
    ('Facturation', {'fields': ['adresse_fact_1', 'adresse_fact_2', 'cp_fact', 'commune_fact']})
    ]


class FournisseurAdmin(admin.ModelAdmin):



admin.site.register(Client, ClientAdmin)
admin.site.register(Fournisseur, FournisseurAdmin)
admin.site.register(Contact, ContactAdmin)
admin.site.register(Affaire, AffaireAdmin)

# Register your models here.
