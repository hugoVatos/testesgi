from django import forms
import logging

from django.contrib.auth.models import Group
from core.utils import create_user_account
from gestion.models.utilisateur import Utilisateur

logger = logging.getLogger('mgl')


class CreateUtilisateurForm(forms.ModelForm):
    role = forms.ModelChoiceField(queryset=Group.objects.all(), widget=forms.Select)
    nom = forms.CharField(max_length=120)
    prenom = forms.CharField(max_length=120)
    poste = forms.CharField(max_length=120, required=False)
    email = forms.EmailField(max_length=20)
    fixe = forms.CharField(max_length=15, required=False)
    portable = forms.CharField(max_length=15, required=False)
    mdp = forms.PasswordInput()
    avatar = forms.ImageField(required=False)
    commentaire = forms.CharField(required=False)

    class Meta:
        model = Utilisateur
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(CreateUtilisateurForm, self).__init__(*args, **kwargs)

        # Ajout des classes
        self.fields['statut'].widget.attrs['class'] = 'form-select'
        self.fields['entreprise'].widget.attrs['class'] = 'form-control'
        self.fields['role'].widget.attrs['class'] = 'form-control'
        self.fields['civilite'].widget.attrs['class'] = 'form-control'
        self.fields['nom'].widget.attrs['class'] = 'form-control'
        self.fields['prenom'].widget.attrs['class'] = 'form-control'
        self.fields['email'].widget.attrs['class'] = 'form-control'
        self.fields['mdp'].widget.attrs['class'] = 'form-control'


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
            utilisateur = create_user_account(email, prenom, nom, mdp)
        except Exception as e:
            raise e

        # Ajout du role
        try:
            role.user_set.add(utilisateur)
        except Exception as e:
            utilisateur.delete()
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
        self.fields['role'].widget.attrs['class'] = 'form-select'
        self.fields['nom'].widget.attrs['class'] = 'form-control'
        self.fields['prenom'].widget.attrs['class'] = 'form-control'
        self.fields['poste'].widget.attrs['class'] = 'form-control'
        self.fields['email'].widget.attrs['class'] = 'form-control'
        self.fields['fixe'].widget.attrs['class'] = 'form-control'
        self.fields['portable'].widget.attrs['class'] = 'form-control'
        self.fields['mdp'].widget.attrs['class'] = 'form-control'
        self.fields['avatar'].widget.attrs['class'] = 'form-control form-control-sm'
        self.fields['commentaire'].widget.attrs['class'] = 'form-control'

    def save(self, commit=True):
        _lp = '%s.save' % self.__class__.__name__
        utilisateur = super(EditUtilisateurForm, self).save(commit=False)
        if commit:
            utilisateur.save()
            self.save_m2m()
        return utilisateur
