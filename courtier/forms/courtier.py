from django import forms
from courtier.models import Courtier


class CourtierForm(forms.ModelForm):

    class Meta:
        model = Courtier
        fields = '__all__'

    def __init__(self, *args, **kwargs):
            super(CourtierForm, self).__init__(*args, **kwargs)



    def save(self, commit=True):
        _lp = '%s.save' % self.__class__.__name__
        courtier = super(CourtierForm, self).save(commit=False)
        if commit:
            courtier.save()
            self.save_m2m()
        return courtier