from django import forms
from tier.models import Tier


class TierForm(forms.ModelForm):

    class Meta:
        model = Tier
        fields = '__all__'

    def __init__(self, *args, **kwargs):
            super(TierForm, self).__init__(*args, **kwargs)



    def save(self, commit=True):
        _lp = '%s.save' % self.__class__.__name__
        tier = super(TierForm, self).save(commit=False)
        if commit:
            tier.save()
            self.save_m2m()
        return tier