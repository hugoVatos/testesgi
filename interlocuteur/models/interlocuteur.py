from django.db import models


class Interlocuteur(models.Model):

    Service = models.CharField(max_length=50, null=True)
    Fonction = models.CharField(max_length=50, null=True)
    Name = models.CharField(max_length=50, null=True)
    Last_Name = models.CharField(max_length=50, null=True)
    Email = models.EmailField(null=True, default="Some String")
    TelM = models.CharField(max_length=50, null=True)
    TelF = models.CharField(max_length=50, null=True)
