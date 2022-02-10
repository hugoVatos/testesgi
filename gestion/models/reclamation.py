from django.db import models
import re


def document_file_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/collaborateur_<id>/paie_pk/<filename>
    clean_filename = re.sub('[\W\_]','',filename)
    return 'reclamation/{0}/{1}'.format(instance.collaborateur.pk, instance.id + '_' + clean_filename)


class Reclamation(models.Model):
    CHOIX_STATUTS = [
        ('en_cours', 'En cours'),
        ('cloture', 'Cloturé')
    ]
    CHOIX_OBJET = [
        ('delai_traitement', 'Délai de traitement'),
        ('non_reception_carte_tier', 'Non réception de carte tiers'),
        ('probleme_expertise', 'Problème d\'expertise'),
        ('augmentation_tarif', 'Augmentation de tarifs'),
        ('Documents_non_recu', 'Documents non reçus'),
        ('autre', 'Autre')
    ]
    statut = models.CharField(max_length=40, choices=CHOIX_STATUTS)
    objet = models.CharField(max_length=40, choices=CHOIX_OBJET)
    date_reclamation = models.DateField(max_length=10)
    date_saisie = models.DateField(max_length=10)
    date_reception = models.DateField(max_length=10)
    date_reponse = models.DateField(max_length=10)
    canal_arrivee = models.CharField(null=False, default=0)
    provenance_reclamation = models.CharField(null=False, default=0)
    client = models.ForeignKey('tier.Tier', on_delete=models.CASCADE)
    assureur = models.CharField('assureur.Assureur', on_delete=models.CASCADE)
    contrat = models.CharField('contrat.Contrat', on_delete=models.CASCADE)
    auteur = models.CharField('core.User', on_delete=models.CASCADE)
    fichier = models.FileField(upload_to=document_file_directory_path)
    commentaire_reclamation = models.TextField(blank=True, null=True)
    commentaire_reponse = models.TextField(blank=True, null=True)

    class Meta:
        verbose_name = "réclamation"
        verbose_name_plural = "réclamations"

    def __str__(self):
        return self.objet

