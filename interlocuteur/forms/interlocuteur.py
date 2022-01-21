from django import forms
from interlocuteur.models import Interlocuteur


class InterlocuteurForm(forms.ModelForm):

    class Meta:
        model = Interlocuteur
        fields = '__all__'

    def __init__(self, *args, **kwargs):
            super(InterlocuteurForm, self).__init__(*args, **kwargs)



    def save(self, commit=True):
        _lp = '%s.save' % self.__class__.__name__
        interlocuteur = super(InterlocuteurForm, self).save(commit=False)
        if commit:
            interlocuteur.save()
            self.save_m2m()
        return interlocuteur