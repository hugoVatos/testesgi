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
    statut = models.CharField(max_length=40, choices=CHOIX_STATUTS, null=False)
    objet = models.CharField(max_length=40, choices=CHOIX_OBJET, null=False)
    date_reclamation = models.DateField(max_length=10, null=False)
    date_saisie = models.DateField(max_length=10, null=False)
    date_reception = models.DateField(max_length=10, null=False)
    date_reponse = models.DateField(max_length=10, null=False)
    canal_arrivee = models.CharField(max_length=10, null=False)
    provenance_reclamation = models.CharField(max_length=10, null=False)
    client = models.ForeignKey('tier.Tier', on_delete=models.DO_NOTHING)
    assureur = models.ForeignKey('assureur.Assureur', on_delete=models.DO_NOTHING)
    contrat = models.CharField(max_length=10)
    auteur = models.ForeignKey('core.Utilisateur', on_delete=models.DO_NOTHING)
    fichier = models.FileField(upload_to=document_file_directory_path, null=False)
    commentaire_reclamation = models.TextField(null=False)
    commentaire_reponse = models.TextField(blank=True, null=True)

    class Meta:
        verbose_name = "réclamation"
        verbose_name_plural = "réclamations"

    def __str__(self):
        return self.objet

