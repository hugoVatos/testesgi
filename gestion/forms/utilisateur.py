from django import forms
import logging

from django.contrib.auth.models import Group
from core.utils import create_user_account
from gestion.models.utilisateur import Utilisateur

logger = logging.getLogger('mgl')


class CreateUtilisateurForm(forms.ModelForm):
    statut = forms.CharField(max_length=20, widget=forms.RadioSelect)
    entreprise = forms.CharField(max_length=20, widget=forms.RadioSelect)
    role = forms.ModelChoiceField(queryset=Group.objects.all(), widget=forms.Select)
    civilite = forms.CharField(max_length=10, required=True)
    nom = forms.CharField(max_length=120, required=True)
    prenom = forms.CharField(max_length=120, required=True)
    email = forms.EmailField(max_length=20, required=True)
    mdp = forms.PasswordInput()
    avatar = forms.ImageField(required=False)

    class Meta:
        model = Utilisateur
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(CreateUtilisateurForm, self).__init__(*args, **kwargs)

        # Ajout des classes
        self.fields['statut'].widget.attrs['class'] = 'radio-inline me-3'
        self.fields['entreprise'].widget.attrs['class'] = 'radio-inline me-3'
        self.fields['role'].widget.attrs['class'] = 'form-control'
        self.fields['civilite'].widget.attrs['class'] = 'form-control'
        self.fields['nom'].widget.attrs['class'] = 'form-control'
        self.fields['prenom'].widget.attrs['class'] = 'form-control'
        self.fields['email'].widget.attrs['class'] = 'form-control'
        self.fields['mdp'].widget.attrs['class'] = 'form-control'
        self.fields['avatar'].widget.attrs['class'] = 'form-control'

    def save(self, commit=True):
        _lp = '%s.save' % self.__class__.__name__
        utilisateur = super(CreateUtilisateurForm, self).save(commit=False)

        prenom = self.cleaned_data.get('prenom', None)
        nom = self.cleaned_data.get('nom', None)
        email = self.cleaned_data.get('email', None)
        mdp = self.cleaned_data.get('mdp', None)
        role = self.cleaned_data.get('role', None)

        # Création de l'utilisateur
        try:
            user = create_user_account(email, prenom, nom, mdp)
        except Exception as e:
            raise e

        # Ajout du role
        try:
            role.user_set.add(user)
        except Exception as e:
            user.delete()
            raise e

        utilisateur.save()
        self.save_m2m()
        return utilisateur


class EditUtilisateurForm(forms.ModelForm):
    class Meta:
        model = Utilisateur
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(EditUtilisateurForm, self).__init__(*args, **kwargs)
        # Ajout des classes
        self.fields['statut'].widget.attrs['class'] = 'form-select'
        self.fields['entreprise'].widget.attrs['class'] = 'form-control'
        self.fields['role'].widget.attrs['class'] = 'form-control'
        self.fields['civilite'].widget.attrs['class'] = 'form-control'
        self.fields['nom'].widget.attrs['class'] = 'form-control'
        self.fields['prenom'].widget.attrs['class'] = 'form-control'
        self.fields['email'].widget.attrs['class'] = 'form-control'
        self.fields['mdp'].widget.attrs['class'] = 'form-control'
        self.fields['avatar'].widget.attrs['class'] = 'form-control'

    def save(self, commit=True):
        _lp = '%s.save' % self.__class__.__name__
        utilisateur = super(EditUtilisateurForm, self).save(commit=False)
        if commit:
            utilisateur.save()
            self.save_m2m()
        return utilisateur
