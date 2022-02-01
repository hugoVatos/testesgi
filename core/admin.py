from django.contrib import admin

# Register your models here.
from django.apps import apps
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext_lazy as _

from core.forms import TaffeUserCreationForm, TaffeUserChangeForm
from core.models import Utilisateur

# Register your models here.
models = apps.get_models()


class TaffeUserAdmin(UserAdmin):
    add_form = TaffeUserCreationForm
    form = TaffeUserChangeForm
    model = Utilisateur
    fieldsets = (
        (None, {'fields': ('email', 'mdp')}),
        (_('Personal info'), {'fields': ('first_name', 'last_name')}),
        (_('Permissions'), {
            'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions'),
        }),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2'),
        }),
    )
    list_display = ('email', 'first_name', 'last_name', 'is_staff')
    list_filter = ('is_staff', 'is_superuser', 'is_active', 'groups')
    search_fields = ('first_name', 'last_name', 'email')
    ordering = ('email',)
    filter_horizontal = ('groups', 'user_permissions',)


admin.site.register(Utilisateur, TaffeUserAdmin)

for model in models:
    try:
        admin.site.register(model)
    except admin.sites.AlreadyRegistered:
        pass
