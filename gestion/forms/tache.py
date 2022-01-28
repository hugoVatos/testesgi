from django import forms
from django.contrib.auth.models import Group
import logging

from gestion.models import Tache
from core.forms import DatetimeInput

logger = logging.getLogger('taffe')



class TacheForm(forms.ModelForm):
    class Meta:
        model = Tache
        fields = ['assignation', 'type', 'customer', 'file', 'object', 'comment', 'deadline']
        widgets = {
            'deadline': DatetimeInput(format='%Y-%m-%dT%H:%M'),
        }

    def __init__(self, *args, **kwargs):
        super(TacheForm, self).__init__(*args, **kwargs)

        # Ajout des classes
        self.fields['assignation'].widget.attrs['class'] = 'form-control selectpicker'
        self.fields['type'].widget.attrs['class'] = 'form-select'
        self.fields['customer'].widget.attrs['class'] = 'form-control selectpicker'
        self.fields['file'].widget.attrs['class'] = 'form-control form-control-sm'
        self.fields['object'].widget.attrs['class'] = 'form-control'
        self.fields['comment'].widget.attrs['class'] = 'form-control'
        self.fields['deadline'].widget.attrs['class'] = 'form-control'
        # Ajout de l'attribut data-live-search
        self.fields['assignation'].widget.attrs['data-live-search'] = 'true'
        self.fields['customer'].widget.attrs['data-live-search'] = 'true'

        self.fields['assignation'].queryset = Utilisateur.objects.get_taffe_users()
