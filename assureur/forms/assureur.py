from django import forms
from assureur.models import Assureur


class AssureurForm(forms.ModelForm):

    class Meta:
        model = Assureur
        fields = '__all__'

    def __init__(self, *args, **kwargs):
            super(AssureurForm, self).__init__(*args, **kwargs)



    def save(self, commit=True):
        _lp = '%s.save' % self.__class__.__name__
        apporteur = super(AssureurForm, self).save(commit=False)
        if commit:
            assureur.save()
            self.save_m2m()
        return assureur