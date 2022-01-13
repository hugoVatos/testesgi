from django.db import models


class Assure(models.Model):
    CLIENT = 'client'
    ANCIEN_CLIENT = 'ancien client'
    PROSPECT = 'prospect'
    ARCHIVE = 'archivé'
    M = 'morale'
    P = 'physique'


    DateCrea = models.DateField(auto_now_add=False, auto_now=False, blank=True, null=True)
    AuteurCrea = models.CharField(max_length=50)
    Datemodif = models.DateField(auto_now_add=False, auto_now=False, blank=True, null=True)
    AuteurModif = models.CharField(max_length=50, blank=True)
    Image = models.FileField(blank=True, null=True)
    VIP = models.BooleanField(blank=False, default=True)
    CodeClient = models.CharField(max_length=50)
    Statut = models.CharField(max_length=50,
                              choices=[
                                  (CLIENT, 'client'),
                                  (ANCIEN_CLIENT, 'ancien client'),
                                  (PROSPECT, 'prospect'),
                                  (ARCHIVE, 'archivé'),
                              ]
                              , null=True)
    typeC = models.CharField(choices=[
        (M, 'morale'),
        (P, 'physique'),

    ], null=True, max_length=50)

    def __str__(self):
        return self.CodeClient

    MONSIEUR = 'MR'
    MADAME = 'MME'
    HOMME = 'H'
    FEMME = 'F'
    Name = models.CharField(max_length=50, null=True)
    Last_Name = models.CharField(max_length=50, null=True)
    Adress = models.CharField(max_length=255, null=True)
    CP = models.CharField(max_length=6, null=True)
    City = models.CharField(max_length=50, null=True)
    Country = models.CharField(max_length=50, null=True)
    Email = models.EmailField(blank=False, default="Some String")
    TelF = models.CharField(max_length=50, null=True)
    TelM = models.CharField(max_length=50, null=True)
    TelP = models.CharField(max_length=50, null=True)
    Birth = models.DateField(auto_now_add=False, auto_now=False, blank=True, null=True)
    BirthLoc = models.CharField(max_length=50, null=True)
    Nationality = models.CharField(max_length=50, null=True)
    Family = models.CharField(max_length=50, null=True)
    Prof = models.CharField(max_length=50, null=True)
    Gel = models.BooleanField(blank=False, default=True)
    CIVIL = models.CharField(max_length=50,
                             choices=[
                                 (MONSIEUR, 'MR'),
                                 (MADAME, 'MME'),
                             ]
                             , null=True)
    SEXE = models.CharField(max_length=50,
                            choices=[
                                (HOMME, 'H'),
                                (FEMME, 'F'),
                            ]
                            , null=True)

    DenoSc = models.CharField(max_length=50, null=True)
    Sigle = models.CharField(max_length=50, null=True)
    StatSc = models.CharField(max_length=50, null=True)
    Siren = models.CharField(max_length=50, null=True)
    Optiflux = models.CharField(max_length=50, null=True)
    Activite = models.CharField(max_length=50, null=True)
    Adress_m = models.CharField(max_length=50, null=True)
    CP_m = models.CharField(max_length=50, null=True)
    City_m = models.CharField(max_length=50, null=True)
    Country_m = models.CharField(max_length=50, null=True)
    NameL = models.CharField(max_length=50, null=True)
    Last_NameL = models.CharField(max_length=50, null=True)
    Email_m = models.EmailField(blank=False, default="Some Stringok", null=True)
    TelF_m = models.CharField(max_length=50, null=True)
    TelM_m = models.CharField(max_length=50, null=True)
    Gel_m = models.BooleanField(blank=False, default=True)
    Rbe = models.BooleanField(blank=False, default=True)

    Relation = models.CharField(max_length=50, null=True)