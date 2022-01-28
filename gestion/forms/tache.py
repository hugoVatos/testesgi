from django import forms

from gestion.models import Tache, Utilisateur


class TacheForm(forms.ModelForm):
    class Meta:
        model = Tache
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(TacheForm, self).__init__(*args, **kwargs)

        # Ajout des classes
        self.fields['type'].widget.attrs['class'] = 'form-select'
        self.fields['date_limite'].widget.attrs['class'] = 'form-control'
        self.fields['statut'].widget.attrs['class'] = 'form-select'
        self.fields['commentaire'].widget.attrs['class'] = 'form-control'
        self.fields['assignation'].widget.attrs['class'] = 'form-control selectpicker'
        self.fields['client'].widget.attrs['class'] = 'form-control selectpicker'
        self.fields['contrat'].widget.attrs['class'] = 'form-control selectpicker'
        self.fields['auteur'].widget.attrs['class'] = 'form-control selectpicker'
        self.fields['date_ajout'].widget.attrs['class'] = 'form-control'

        # Ajout de l'attribut data-live-search
        self.fields['assignation'].widget.attrs['data-live-search'] = 'true'
        self.fields['client'].widget.attrs['data-live-search'] = 'true'
        self.fields['auteur'].widget.attrs['data-live-search'] = 'true'

        self.fields['assignation'].queryset = Utilisateur.objects.get_taffe_users()
