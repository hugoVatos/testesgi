from django.db import models

class Assureur(models.Model):
    #assureur
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
    Adress_A = models.CharField(max_length=50)
    CP_A = models.CharField(max_length=50, null=True)
    City_A = models.CharField(max_length=50, null=True)
    Country_A = models.CharField(max_length=50, null=True)


    #mandat
    T = 'Montant 100%'
    C = 'Montant par compagnie'
    Faculte = models.FloatField()
    Corps = models.FloatField()
    plafond = models.CharField(choices=[
        (T, 'Montant 100%'),
        (C, 'Montant par compagnie')], max_length=50)
    Mont_Faculte = models.FloatField()
    Mont_Corps = models.FloatField()
    Date_Mandat = models.DateField()
    Date_Fin_Mandat = models.DateField()
    Mandat = models.FileField()
    Tampon = models.FileField()


    #commission
    Rc = models.DecimalField(max_digits=5, decimal_places=2)
    Com_Corps = models.DecimalField(max_digits=5, decimal_places=2)
    Com_Fac = models.DecimalField(max_digits=5, decimal_places=2)
    Plaisance = models.DecimalField(max_digits=5, decimal_places=2)

    #Complement
    Date_Optiflux = models.DateField()
    Date_Fin_Optiflux = models.DateField()
    Cesam = models.FloatField()
    Pb = models.FloatField()
    Bdi = models.FloatField()
    Code_bureau = models.FloatField()

