from django.db import models
from interlocuteur.models import Interlocuteur


class Tier(models.Model):
    Agent = 'Agent'
    Agent_aperiteur = 'Agent Apériteur'
    Beneficiaire = 'Bénéficiaire'
    Expert = 'Expert'
    Avocat = 'Avocat'

    Statut = models.CharField(max_length=50,
                              choices=[
                                  (Agent, 'Agent'),
                                  (Agent_aperiteur, 'Agent Apériteur'),
                                  (Beneficiaire, 'Bénéficiaire'),
                                  (Expert, 'Expert'),
                                  (Avocat, 'Avocat'),
                              ]
                              , null=True)
    Bdi = models.FloatField()
    Optiflux = models.FloatField()
    Image = models.FileField(blank=True, null=True)
    DenoSc = models.CharField(max_length=50, null=True)
    StatSc = models.CharField(max_length=50, null=True)
    Siren = models.CharField(max_length=50, null=True)
    Adress1 = models.CharField(max_length=50)
    Adress2 = models.CharField(max_length=50)
    Adress3 = models.CharField(max_length=50)
    CP = models.CharField(max_length=50, null=True)
    City = models.CharField(max_length=50, null=True)
    Country = models.CharField(max_length=50, null=True)
    Interlocuteur = models.ForeignKey(Interlocuteur, on_delete=models.CASCADE)