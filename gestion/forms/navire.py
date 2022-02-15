from django import forms

from gestion.models import Navire, Moteur


class NavireForm(forms.ModelForm):
    nom_navire = forms.CharField(max_length=60)
    immatriculation = forms.CharField(max_length=40)
    type = forms.CharField(max_length=40)
    pavillon = forms.CharField(max_length=40)
    annee = forms.CharField(max_length=5)
    tonnage_gt = forms.IntegerField()
    tonnage_tjb = forms.IntegerField()
    longueur = forms.IntegerField()
    largeur = forms.IntegerField()
    code_imo = forms.CharField(max_length=40)
    materiaux = forms.CharField(max_length=40)
    classe = forms.CharField(max_length=40)
    port_attache = forms.CharField(max_length=100)

    class Meta:
        model = Navire
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(NavireForm, self).__init__(*args, **kwargs)

        # Ajout des classes
        self.fields['nom_navire'].widget.attrs['class'] = 'form-control'
        self.fields['immatriculation'].widget.attrs['class'] = 'form-control'
        self.fields['type'].widget.attrs['class'] = 'form-control'
        self.fields['pavillon'].widget.attrs['class'] = 'form-control'
        self.fields['annee'].widget.attrs['class'] = 'form-control'
        self.fields['tonnage_gt'].widget.attrs['class'] = 'form-control'
        self.fields['tonnage_tjb'].widget.attrs['class'] = 'form-control'
        self.fields['longueur'].widget.attrs['class'] = 'form-control'
        self.fields['largeur'].widget.attrs['class'] = 'form-control'
        self.fields['code_imo'].widget.attrs['class'] = 'form-control'
        self.fields['materiaux'].widget.attrs['class'] = 'form-control'
        self.fields['classe'].widget.attrs['class'] = 'form-control'
        self.fields['port_attache'].widget.attrs['class'] = 'form-control'

    def save(self, commit=True):
        _lp = '%s.save' % self.__class__.__name__
        navire = super(NavireForm, self).save(commit=False)
        if commit:
            navire.save()
            self.save_m2m()
        return navire


class MoteurForm(forms.ModelForm):
    puissance_tot = forms.IntegerField()
    carburant = forms.CharField(max_length=30)
    annee = forms.CharField(max_length=5)
    type = forms.CharField(max_length=40)
    marque = forms.CharField(max_length=100)
    nombre = forms.IntegerField()

    class Meta:
        model = Moteur
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(MoteurForm, self).__init__(*args, **kwargs)

        # Ajout des classes
        self.fields['puissance_tot'].widget.attrs['class'] = 'form-control'
        self.fields['carburant'].widget.attrs['class'] = 'form-control'
        self.fields['annee'].widget.attrs['class'] = 'form-control'
        self.fields['type'].widget.attrs['class'] = 'form-control'
        self.fields['marque'].widget.attrs['class'] = 'form-control'
        self.fields['nombre'].widget.attrs['class'] = 'form-control'

    def save(self, commit=True):
        _lp = '%s.save' % self.__class__.__name__
        moteur = super(MoteurForm, self).save(commit=False)
        if commit:
            moteur.save()
            self.save_m2m()
        return moteur


