from django.db import models


class Navire(models.Model):
    nom_navire = models.CharField(max_length=60)
    immatriculation = models.CharField(max_length=40, primary_key=True)
    type = models.CharField(max_length=40)
    pavillon = models.CharField(max_length=40)
    annee = models.CharField(max_length=5)
    tonnage_gt = models.PositiveIntegerField(null=False, default=0)
    tonnage_tjb = models.PositiveIntegerField(null=False, default=0)
    longueur = models.PositiveIntegerField(null=False, default=0)
    largeur = models.PositiveIntegerField(null=False, default=0)
    code_imo = models.CharField(max_length=40)
    materiaux = models.CharField(max_length=40)
    classe = models.CharField(max_length=40)
    port_attache = models.CharField(max_length=100)

    moteur = models.ManyToManyField('Moteur')

    class Meta:
        verbose_name = "navire"
        verbose_name_plural = "navires"

    def __str__(self):
        return self.nom_navire


class Moteur(models.Model):
    puissance_tot = models.IntegerField()
    carburant = models.CharField(max_length=30)
    annee = models.CharField(max_length=5)
    type = models.CharField(max_length=40)
    marque = models.CharField(max_length=100)
    nombre = models.IntegerField(null=False, default=0)

    class Meta:
        verbose_name = "moteur"
        verbose_name_plural = "moteurs"

    def __str__(self):
        return 'puissance: {0} - carburant: {1}' % {self.puissance_tot, self.carburant}
