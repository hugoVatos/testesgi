from gestion.models.reclamation import Reclamation
from django import forms


class ReclamationForm(forms.ModelForm):

    class Meta:
        model = Reclamation
        fields = '__all__'

    def __init__(self, *args, **kwargs):
            super(ReclamationForm, self).__init__(*args, **kwargs)

            # Ajout des classes
            self.fields['statut'].widget.attrs['class'] = 'form-control'
            self.fields['objet'].widget.attrs['class'] = 'form-control'
            self.fields['date_reclamation'].widget.attrs['class'] = 'form-control'
            self.fields['date_saisie'].widget.attrs['class'] = 'form-control'
            self.fields['date_reception'].widget.attrs['class'] = 'form-control'
            self.fields['date_reponse'].widget.attrs['class'] = 'form-control'
            self.fields['canal_arrivee'].widget.attrs['class'] = 'form-control'
            self.fields['provenance_reclamation'].widget.attrs['class'] = 'form-control'
            self.fields['client'].widget.attrs['class'] = 'form-control'
            self.fields['assureur'].widget.attrs['class'] = 'form-control'
            self.fields['contrat'].widget.attrs['class'] = 'form-control'
            self.fields['auteur'].widget.attrs['class'] = 'form-control'
            self.fields['fichier'].widget.attrs['class'] = 'form-control'
            self.fields['commentaire_reclamation'].widget.attrs['class'] = 'form-control'
            self.fields['commentaire_reponse'].widget.attrs['class'] = 'form-control'

    def save(self, commit=True):
        _lp = '%s.save' % self.__class__.__name__
        reclamation = super(ReclamationForm, self).save(commit=False)
        if commit:
            reclamation.save()
            self.save_m2m()
        return reclamation
