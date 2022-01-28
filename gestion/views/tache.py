import logging
from django.contrib import messages
from django.core.exceptions import PermissionDenied
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.views.generic import TemplateView
from django.urls import reverse

from gestion.forms import TacheForm
from gestion.models import Tache

logging.getLogger('taffe')

class CreateTacheView(TemplateView):
    template_name = 'gestion/tache-nouveau.html'
    permissions = ['gestion.add_task']
    form_class = TacheForm

    def get_context_data(self, form=None, *args, **kwargs):
        context = super(CreateTacheView, self).get_context_data(**kwargs)
        executor = self.request.user
        context['form'] = form if form else self.form_class()
        if not executor.is_administrator:
            context['form'].fields['assignation'].initial = executor
            context['form'].fields['assignation'].widget.attrs['disabled'] = 'true'
        return context

    def post(self, request, **kwargs):
        executor = self.request.user
        _lp = '[%s] %s.post' % (executor, self.__class__.__name__)
        request = super(CreateTacheView, self).post(**kwargs)
        form = self.form_class(request.POST)
        context = self.get_context_data(form=form, **kwargs)
        if not form.is_valid():
            return self.render_to_response(context, status=400)
        # create the task
        try:
            task = form.save()
        except Exception as e:
            _msg = 'Une erreur (%s) est survenue lors de la création de la tâche %s: %s' % (
                type(e).__name__, self.request.POST['object'], e)
            logger.error('%s %s' % (_lp, _msg))
            messages.add_message(request, messages.ERROR, message=_msg)
            return self.render_to_response(context, status=500)
        else:
            _msg = 'Tâche créé avec succès'
            logger.info('%s %s' % (_lp, _msg))
            messages.add_message(request, messages.INFO, message=_msg)
        return self.render_to_response(context, status=201)


class EditTacheView(TemplateView):
    template_name = 'account/edit-task.html'
    permissions = ['account.change_task']
    form_class = TacheForm

    def get_context_data(self, form=None, *args, **kwargs):
        context = super(EditTacheView, self).get_context_data(**kwargs)
        executor = self.request.user
        task = get_object_or_404(Tache, pk=kwargs.get('pk'))
        context['form'] = form if form else self.form_class(instance=task)
        if not executor.is_administrator:
            context['form'].fields['assignation'].widget.attrs['disabled'] = 'true'
        return context

    def post(self, request, **kwargs):
        executor = self.request.user
        _lp = '[%s] %s.post' % (executor, self.__class__.__name__)
        request = super(EditTacheView, self).post(**kwargs)
        task = get_object_or_404(Tache, pk=kwargs.get('pk'))
        form = self.form_class(request.POST, request.FILES, instance=task)
        context = self.get_context_data(form=form, **kwargs)
        if not form.is_valid():
            return self.render_to_response(context, status=400)
        # create the task
        try:
            task = form.save()
        except Exception as e:
            _msg = 'Une erreur (%s) est survenue lors de la modification de la tâche %s: %s' % (
                type(e).__name__, self.request.POST['object'], e)
            logger.error('%s %s' % (_lp, _msg))
            messages.add_message(request, messages.ERROR, message=_msg)
            return self.render_to_response(context, status=500)
        else:
            _msg = 'Tâche modifiée avec succès'
            logger.info('%s %s' % (_lp, _msg))
            messages.add_message(request, messages.INFO, message=_msg)
        return self.render_to_response(context, status=200)


class EditTacheStatusView(TemplateView):
    permissions = ['gestion.change_task']

    def get(self, request, *args, **kwargs):
        tache = get_object_or_404(Tache, pk=kwargs.get('pk'))
        tache.done = not tache.done
        try:
            tache.save()
            messages.add_message(request, messages.INFO, message='Tâche #%s mise à jour avec succès' % tache.id)
        except Exception as e:
            messages.add_message(request, messages.ERROR,
                                 message='Erreur (%s) lors de la mise à jour de la tâche #%s : %s' % (
                                     type(e).__name__, tache.id, e))
        return HttpResponseRedirect(reverse('account:task-my-list'))


class ListTacheView(TemplateView):
    template_name = 'gestion/tache-gestion.html'
    permissions = ['gestion.view_task']

    def get_context_data(self, *args, **kwargs):
        executor = self.request.user
        logger.debug('groups: %s' % executor.groups.filter(name='Administrateur').exists())
        if not executor.is_superuser or not executor.groups.filter(name='Administrateur').exists():
            raise PermissionDenied
        _lp = '[%s] %s.get_context_data' % (executor, self.__class__.__name__)
        context = super(ListTacheView, self).get_context_data(**kwargs)
        taches = Tache.objects.all()
        context['taches'] = taches
        return context


class ListUtilisateurTacheView(TemplateView):
    template_name = 'account/list-my-task.html'
    permissions = ['account.view_task']

    def get_context_data(self, *args, **kwargs):
        executor = self.request.user
        _lp = '[%s] %s.get_context_data' % (executor, self.__class__.__name__)
        context = super(ListUtilisateurTacheView, self).get_context_data(**kwargs)
        taches = Tache.objects.filter(assignation=executor)
        context['taches'] = taches
        return context
