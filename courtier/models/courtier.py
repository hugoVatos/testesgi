from django.db import models

class Courtier(models.Model):
    #assureur
    Image = models.FileField(blank=True, null=True)
    DenoSc = models.CharField(max_length=50, null=True)
    StatSc = models.CharField(max_length=50, null=True)
    Siren = models.CharField(max_length=50, null=True)
    Adress = models.CharField(max_length=50)
    CP = models.CharField(max_length=50, null=True)
    City = models.CharField(max_length=50, null=True)
    Country = models.CharField(max_length=50, null=True)
    Adress_Rattachement = models.CharField(max_length=50)
    CP_Rattachement = models.CharField(max_length=50, null=True)
    City_Rattachement = models.CharField(max_length=50, null=True)
    Country_Rattachement = models.CharField(max_length=50, null=True)
    Bdi = models.FloatField()
    Cesam = models.FloatField()
    Convention = models.FileField

    #Taux
    Taux_Rc = models.DecimalField(max_digits=5, decimal_places=2)
    Taux_Corps = models.DecimalField(max_digits=5, decimal_places=2)
    Taux_Fac = models.DecimalField(max_digits=5, decimal_places=2)
    Taux_Plaisance = models.DecimalField(max_digits=5, decimal_places=2)


