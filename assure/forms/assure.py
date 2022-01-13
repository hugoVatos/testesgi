from django import forms
from assure.models import Assure


class AssureForm(forms.ModelForm):

    class Meta:
        model = Assure
        fields = '__all__'

    def __init__(self, *args, **kwargs):
            super(AssureForm, self).__init__(*args, **kwargs)



    def save(self, commit=True):
        _lp = '%s.save' % self.__class__.__name__
        assure = super(AssureForm, self).save(commit=False)
        if commit:
            assure.save()
            self.save_m2m()
        return assure