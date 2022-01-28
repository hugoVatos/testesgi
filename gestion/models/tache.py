from django.db import models


class TacheType(models.Model):
    class Meta:
        verbose_name = "type de tâche"
        verbose_name_plural = "types de tâches"


def tache_file_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    return 'users/{0}/{1}'.format(instance.assignation.pk, filename)


class Tache(models.Model):
    assignation = models.ForeignKey('tier.Tier', on_delete=models.CASCADE)
    type = models.ForeignKey(TacheType, on_delete=models.CASCADE)
    interlocuteur = models.ForeignKey('gestion.Utilisateur', on_delete=models.CASCADE, blank=True, null=True)
    file = models.FileField(upload_to=tache_file_directory_path, null=True, blank=True)
    object = models.CharField(max_length=120)
    comment = models.TextField(blank=True, null=True)
    deadline = models.DateTimeField(null=True, blank=True)
    done = models.BooleanField(default=False)

    class Meta:
        verbose_name = "tâche"
        verbose_name_plural = "tâches"

    def __str__(self):
        return self.object
