from django.db import models

class Apporteur(models.Model):

    SAS = 'SAS'
    SARL = 'SARL'
    Type_1 = 'type 1'
    Type_2 = 'type 2'
    France = 'france'
    Suisse = 'suisse'
    Monaco = 'monaco'
    Option_1 = 'option 1'
    Option_2 = 'option 2'
    Option_3 = 'option 3'


    Image = models.FileField(blank=True, null=True)
    DenoSc = models.CharField(max_length=50, null=True)
    Siren = models.CharField(max_length=50, null=True)
    StatSc = models.CharField(max_length=50, choices=[
                                                        (SAS, 'SAS'),
                                                        (SARL, 'SARL')
                                                    ], null=True)
    Type_Apporteur = models.CharField(max_length=50, default="", choices=[
                                                        (Type_1, 'type 1'),
                                                        (Type_2, 'type 2')
                                                    ], null=True)
    Adress_siege1 = models.CharField(max_length=50)
    Adress_siege2 = models.CharField(max_length=50)
    Adress_siege3 = models.CharField(max_length=50)

    CP = models.CharField(max_length=50)
    City = models.CharField(max_length=50)
    Country = models.CharField(max_length=50, choices=[
                                                    (France, 'france'),
                                                    (Suisse, 'suisse'),
                                                    (Monaco, 'monaco'),
                                                    (Option_1, 'option 1'),
                                                    (Option_2, 'option 2'),
                                                    (Option_3, 'option 3')
                                                    ], null=True)
    Email = models.EmailField(null=True, default="Some String")
    Mdp = models.CharField(max_length=50, null=True)
    Convention = models.FileField(blank=True, null=True)
    ExtraPrime = models.DecimalField(max_digits=5, decimal_places=2)
    CoCourtage = models.DecimalField(max_digits=5, decimal_places=2)