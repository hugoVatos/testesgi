import logging

from django.contrib import messages
from django.contrib.auth.forms import PasswordChangeForm
from django.shortcuts import get_object_or_404
from django.views.generic import TemplateView

from gestion.forms import CreateUtilisateurForm, EditUtilisateurForm
from core.models import Utilisateur
from gestion.models import Utilisateur

logger = logging.getLogger('taffe')


class CreateUtilisateurView(TemplateView):
    template_name = 'gestion/utilisateur-nouveau.html'
    form_class = CreateUtilisateurForm
    permissions = ['gestion.add_user']

    def get_context_data(self, form=None, **kwargs):
        context = super(CreateUtilisateurView, self).get_context_data(**kwargs)
        context['form'] = form if form else self.form_class()
        return context

    def post(self, request, **kwargs):
        context = self.get_context_data(**kwargs)
        form = self.form_class(request.POST)

        if not form.is_valid():
            return self.render_to_response(context, status=400)
        try:
            collaborateur = form.save()
        except Exception as e:
            _msg = 'Une erreur (%s) est survenue lors de la création de l\'utilisateur : %s' % (type(e).__name__, e)
            messages.add_message(request, messages.ERROR,
                                 message="Une erreur est survenue lors de la création de l\'utilisateur")
        else:
            _msg = 'Collaborateur %s crée avec succès' % collaborateur.email
            messages.add_message(request, messages.INFO, message="Utilisateur crée avec succès")
        return self.render_to_response(context, status=201)


class ListUtilisateurView(TemplateView):
    template_name = 'gestion/utilisateur-gestion.html'
    permissions = ['gestion.view_user']

    def get_context_data(self, *args, **kwargs):
        context = super(ListUtilisateurView, self).get_context_data(**kwargs)
        context['utilisateurs'] = Utilisateur.objects.all()
        return context


class EditUtilisateurView(TemplateView):
    template_name = 'gestion/utilisateur-nouveau.html'
    form_class = EditUtilisateurForm
    form_change_password_class = PasswordChangeForm

    def get_context_data(self, form=None, *args, **kwargs):
        utilisateur = get_object_or_404(Utilisateur, pk=kwargs.get('pk'))
        context = super(EditUtilisateurView, self).get_context_data(**kwargs)
        context['form'] = form if form else self.form_class(instance=utilisateur)
        return context

    def post(self, request, **kwargs):
        utilisateur = get_object_or_404(Utilisateur, pk=kwargs.get('pk'))
        _lp = '%s.post' % self.__class__.__name__

        form = self.form_class(data=request.POST, instance=utilisateur)
        context = self.get_context_data(form=form, **kwargs)
        if not form.is_valid():
            return self.render_to_response(context, status=400)
        try:
            utilisateur = form.save()
        except Exception as e:
            _msg = 'Une erreur (%s) est survenue lors de la mise à jour du collaborateur : %s' % (type(e).__name__, e)
            messages.add_message(request, messages.ERROR,
                                 message="Une erreur est survenue lors de la mise à jour du collaborateur")
        else:
            _msg = 'Collaborateur %s crée avec succès' % utilisateur.email
            messages.add_message(request, messages.INFO, message="Collaborateur crée avec succès")
        return self.render_to_response(context, status=201)

