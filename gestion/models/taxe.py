from django.db import models


class Taxe(models.Model):
    TYPE_CHOICES = [
        ('assurance_terre_air','Assurance Transports terrestres et aériens'),
        ('assurance_maritime', 'Assurance maritime : Sport, plaisance'),
        ('navire_peche', 'Navire de pêche, commerce'),
        ('fgti', 'FGTI'),
        ('autres', 'Autres'),
    ]

    type = models.CharField(max_length=40, choices=TYPE_CHOICES, null=False)
    intitule = models.CharField(max_length=120, null=False)
    annee = models.DateField(null=False)
    assiette = models.IntegerField(max_length=10, null=False)
    taux = models.FloatField(max_length=3, null=False)
    montant = models.FloatField(null=False)

    class Meta:
        verbose_name = "taxe"
        verbose_name_plural = "taxes"
