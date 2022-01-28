from __future__ import unicode_literals

from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin, AbstractUser
from django.db import models

from core.managers import UserManager


class User(AbstractUser):
    username = None
    email = models.EmailField('email address', unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserManager()

    class Meta:
        verbose_name = "utilisateur"
        verbose_name_plural = "utilisateurs"

    def __str__(self):
        return self.get_full_name()

    def has_group_perms(self, permissions):
        for perm in permissions:
            if perm not in self.get_group_permissions():
                return False
        return True

    @property
    def is_customer(self):
        return self.groups.filter(name="Apporteur").exists()

    @property
    def is_commercial(self):
        return self.groups.filter(name="Tier").exists()

    @property
    def is_preparer(self):
        return self.groups.filter(name="Assure").exists()

    @property
    def is_collaborator(self):
        return self.groups.filter(name="Assureur").exists()

    @property
    def is_faconnier(self):
        return self.groups.filter(name="Courtier").exists()

    @property
    def is_administrator(self):
        return self.groups.filter(name="Administrateur").exists()
