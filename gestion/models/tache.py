from django.db import models
from django.utils import timezone


class TacheType(models.Model):
    class Meta:
        verbose_name = "type de tâche"
        verbose_name_plural = "types de tâches"


def tache_file_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    return 'users/{0}/{1}'.format(instance.assignation.pk, filename)


class Tache(models.Model):

    TYPE_TACHE_CHOICES = [
        ('rdv-tel', 'Rdv téléphonique'),
        ('rdv-phy', 'Rdv physique'),
        ('relance', 'Relance'),
        ('lettre', 'Envoie lettre recommandée'),
        ('avenant', 'Création d\'avenant'),
        ('autre', 'Autres')
    ]
    STATUT_CHOICES = [
        ('en-cours', 'En cours'),
        ('termine', 'Terminée')
    ]
    type = models.ForeignKey(TacheType, on_delete=models.CASCADE)
    date_limite = models.DateTimeField(default=timezone.now)
    statut = models.CharField(max_length=30, choices=STATUT_CHOICES)
    commentaire = models.TextField(blank=True, null=True)
    assignation = models.ForeignKey('gestion.Utilisateur', on_delete=models.CASCADE, blank=True, null=True)
    client = models.ForeignKey('tier.Tier', on_delete=models.CASCADE, blank=True, null=True)
    contrat = models.CharField(max_length=30, blank=True, null=True)
    # auteur = models.ForeignKey('gestion.Utilisateur', on_delete=models.CASCADE, blank=True, null=True)
    date_ajout = models.DateTimeField(auto_now=True)
    done = models.BooleanField(default=False)

    class Meta:
        verbose_name = "tâche"
        verbose_name_plural = "tâches"

    def __str__(self):
        return self.commentaire
