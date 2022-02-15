from django import forms

from gestion.models import Risque


class RisqueForm(forms.ModelForm):

    class Meta:
        model = Risque
        fields = '__all__'

    def __init__(self, *args, **kwargs):
            super(RisqueForm, self).__init__(*args, **kwargs)

            # Ajout des classes
            self.fields['type'].widget.attrs['class'] = 'form-control'
            self.fields['intitule'].widget.attrs['class'] = 'form-control'
            self.fields['assureur'].widget.attrs['class'] = 'form-control'
            self.fields['doc_cg'].widget.attrs['class'] = 'custom-file-input'
            self.fields['doc_ipid'].widget.attrs['class'] = 'custom-file-input'
            self.fields['doc_fc'].widget.attrs['class'] = 'custom-file-input'
            self.fields['doc_cp'].widget.attrs['class'] = 'custom-file-input'

    def save(self, commit=True):
        _lp = '%s.save' % self.__class__.__name__
        risque = super(RisqueForm, self).save(commit=False)
        if commit:
            risque.save()
            self.save_m2m()
        return risque
