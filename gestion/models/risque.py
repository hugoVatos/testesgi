import re

from django.db import models


def document_file_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/collaborateur_<id>/paie_pk/<filename>
    clean_filename = re.sub('[\W\_]','',filename)
    return 'risque/{0}/{1}'.format(instance.type, instance.id + '_' + clean_filename)


class Risque(models.Model):
    TYPE_CHOICES = [
        ('maritime','Maritime'),
        ('terrestre', 'Terrestre'),
        ('aerien', 'Aérien'),
        ('autre', 'Autre'),
    ]

    type = models.CharField(max_length=40, choices=TYPE_CHOICES, null=False)
    intitule = models.CharField(max_length=120, null=False)
    assureur = models.ForeignKey('assureur.Assureur', on_delete=models.DO_NOTHING)
    doc_cg = models.FileField(upload_to=document_file_directory_path, null=False)
    doc_ipid = models.FileField(upload_to=document_file_directory_path, null=False)
    doc_fc = models.FileField(upload_to=document_file_directory_path, null=False)
    doc_cp = models.FileField(upload_to=document_file_directory_path, null=False)

    class Meta:
        verbose_name = "risque"
        verbose_name_plural = "risques"
