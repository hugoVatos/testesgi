from django import forms

from django.contrib.auth.models import Group
from core.utils import create_user_account
from gestion.models.utilisateur import Utilisateur


class CreateUtilisateurForm(forms.ModelForm):

    class Meta:
        model = Utilisateur
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(CreateUtilisateurForm, self).__init__(*args, **kwargs)

        # Ajout des classes
        self.fields["statut"].widget = forms.RadioSelect(choices=self.fields["statut"].choices,
                                                         attrs={"class": "radio-inline me-3"})
        self.fields["entreprise"].widget = forms.RadioSelect(choices=self.fields["entreprise"].choices,
                                                         attrs={"class": "radio-inline me-3"})
        self.fields['role'].widget.attrs['class'] = 'dropdown-groups form-select'
        self.fields['civilite'].widget.attrs['class'] = 'dropdown-groups form-select'
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
        self.fields["statut"].widget = forms.RadioSelect(choices=self.fields["statut"].choices,
                                                         attrs={"class": "radio-inline me-3"})
        self.fields["entreprise"].widget = forms.RadioSelect(choices=self.fields["entreprise"].choices,
                                                             attrs={"class": "radio-inline me-3"})
        self.fields['role'].widget.attrs['class'] = 'dropdown-groups form-select'
        self.fields['civilite'].widget.attrs['class'] = 'dropdown-groups form-select'
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
