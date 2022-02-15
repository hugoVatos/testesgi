from django.contrib.auth.models import AbstractUser
from django.db import models
from core.managers import UserManager


class Utilisateur(AbstractUser):
    username = None
    email = models.EmailField("adresse email", unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserManager()

    def __str__(self):
        return self.get_full_name()

    def has_group_perms(self, permissions):
        for perm in permissions:
            if perm not in self.get_group_permissions():
                return False
        return True

    @property
    def is_apporteur(self):
        return self.groups.filter(name="Apporteur").exists()
