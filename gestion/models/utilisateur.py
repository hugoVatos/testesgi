from django.conf.global_settings import MEDIA_URL
from django.db import models


def user_directory_path(instance, filename):
    return '/media/users/{0}/{1}'.format(instance, filename)

class Utilisateur(models.Model):
    TYPE_USER_CHOICE = [
        ('actif', 'Actif'),
        ('non-actif', 'Non Actif')
    ]
    COMPANY_CHOICES = [
        ('taffe', 'Taffe'),
        ('gruvel', 'Gruvel'),
        ('delta', 'Delta'),
    ]
    GENDER_CHOICE = [
        ('masculin', 'M'),
        ('feminin', 'Mme')
    ]
    statut = models.CharField(max_length=10, choices=TYPE_USER_CHOICE)
    entreprise = models.CharField(max_length=10, choices=COMPANY_CHOICES)
    role = models.CharField(max_length=30, default='Commerce')
    civilite = models.CharField(max_length=10, choices=GENDER_CHOICE)
    nom = models.CharField(max_length=120)
    prenom = models.CharField(max_length=120)
    email = models.CharField(max_length=20)
    mdp = models.CharField(max_length=100)
    avatar = models.ImageField(upload_to=user_directory_path, null=True, blank=True,
                               default='static/images/equipe/25.jpg')

    class Meta:
        verbose_name = "utilisateur"
        verbose_name_plural = "utilisateurs"

    def __str__(self):
        return '%s %s' % (self.prenom, self.nom)

    @property
    def get_avatar(self):
        return '{0}{1}'.format(MEDIA_URL, self.avatar)
