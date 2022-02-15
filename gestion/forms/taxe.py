from django import forms

from gestion.models import Taxe


class TaxeForm(forms.ModelForm):

    class Meta:
        model = Taxe
        fields = '__all__'

    def __init__(self, *args, **kwargs):
            super(TaxeForm, self).__init__(*args, **kwargs)

            # Ajout des classes
            self.fields['type'].widget.attrs['class'] = 'form-control'
            self.fields['intitule'].widget.attrs['class'] = 'form-control'
            self.fields['annee'].widget.attrs['class'] = 'form-control'
            self.fields['assiette'].widget.attrs['class'] = 'custom-file-input'
            self.fields['taux'].widget.attrs['class'] = 'custom-file-input'
            self.fields['montant'].widget.attrs['class'] = 'custom-file-input'

    def save(self, commit=True):
        _lp = '%s.save' % self.__class__.__name__
        taxe = super(TaxeForm, self).save(commit=False)
        if commit:
            taxe.save()
            self.save_m2m()
        return taxe
