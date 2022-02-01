from django import forms

from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import Utilisateur


class TaffeUserCreationForm(UserCreationForm):
    class Meta:
        model = Utilisateur
        fields = ('email', 'password')


class TaffeUserChangeForm(UserChangeForm):
    class Meta:
        model = Utilisateur
        fields = ('email', 'password')


class DateInput(forms.DateInput):
    input_type = 'date'
    