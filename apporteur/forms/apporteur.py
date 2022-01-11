from django import forms
from apporteur.models import Apporteur


class ApporteurForm(forms.ModelForm):

    class Meta:
        model = Apporteur
        fields = '__all__'

    def __init__(self, *args, **kwargs):
            super(ApporteurForm, self).__init__(*args, **kwargs)



    def save(self, commit=True):
        _lp = '%s.save' % self.__class__.__name__
        apporteur = super(ApporteurForm, self).save(commit=False)
        if commit:
            apporteur.save()
            self.save_m2m()
        return apporteur