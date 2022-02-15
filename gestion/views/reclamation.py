import logging

from django.http import HttpResponse, StreamingHttpResponse
from django.views.generic import TemplateView
from django.contrib import messages
from django.shortcuts import get_object_or_404

from core.utils import download
from gestion.models import Reclamation

from gestion.forms import ReclamationForm


class CreateReclamationView(TemplateView):
    template_name = 'gestion/reclamation-nouveau.html'
    form_class = ReclamationForm

    def get_context_data(self, form=None, *args, **kwargs):
        context = super(CreateReclamationView, self).get_context_data(**kwargs)
        context['form'] = form if form else self.form_class()
        return context

    def post(self, request, **kwargs):
        context = self.get_context_data(**kwargs)
        form = self.form_class(request.POST, request.FILES)

        if not form.is_valid():
            context['form'] = form
            return self.render_to_response(context, status=400)
        try:
            reclamation = form.save()
        except Exception as e:
            _msg = 'Une erreur (%s) est survenue lors de la création de la réclamation : %s' % (type(e).__name__, e)
            messages.add_message(request, messages.ERROR,
                                 message="Une erreur est survenue lors de la création de la réclamation")
        else:
            _msg = 'Réclamation %s (%s) créee avec succès' % (reclamation.objet, reclamation.statut)
            messages.add_message(request, messages.INFO, message="Réclamation créee avec succès")
        return self.render_to_response(context, status=201)


class EditReclamationView(TemplateView):
    template_name = 'gestion/reclamation-modification.html'
    form_class = ReclamationForm

    def get_context_data(self, form=None, *args, **kwargs):
        context = super(EditReclamationView, self).get_context_data(**kwargs)
        reclamation = get_object_or_404(Reclamation, pk=kwargs.get('pk'))
        context['form'] = form if form else self.form_class(instance=reclamation)
        return context

    def post(self, request, **kwargs):
        reclamation = get_object_or_404(Reclamation, pk=kwargs.get('pk'))
        form = self.form_class(request.POST, instance=reclamation)
        if not form.is_valid():
            context = self.get_context_data(form=form, **kwargs)
            return self.render_to_response(context, status=400)
        # edite la réclamation
        try:
            reclamation = form.save()
        except Exception as e:
            _msg = 'Une erreur (%s) est survenue lors de la modification de la réclamation %s: %s' % (
                type(e).__name__, self.request.POST['label'], e)
            messages.add_message(request, messages.ERROR, message=_msg)
            context = self.get_context_data(form=form, **kwargs)
            return self.render_to_response(context, status=500)
        else:
            _msg = 'Réclamation de %s %s modifié avec succès' % (reclamation.objects, reclamation.statut)
            messages.add_message(request, messages.INFO, message=_msg)
        context = self.get_context_data(**kwargs)
        return self.render_to_response(context, status=200)


def download_reclamation(request, pk):
    reclamation = Reclamation.objects.filter(pk=pk)[0]
    filename = reclamation.fiche_pdf
    name = str(filename).split('/')[-1]

    response = download(request, pk, filename, name)
    return response


class ListReclamationView(TemplateView):
    template_name = 'gestion/reclamation-gestion.html'

    def get_context_data(self, *args, **kwargs):
        context = super(ListReclamationView, self).get_context_data(**kwargs)
        context['reclamations'] = Reclamation.objects.all()

        return context
