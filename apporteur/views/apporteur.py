from django.contrib import messages
from django.shortcuts import get_object_or_404

from apporteur.models import Apporteur
from apporteur.forms import ApporteurForm
from django.views.generic.base import TemplateView

class CreateApporteurView(TemplateView):
    form_class = ApporteurForm
    template_name = 'apporteurs/apporteur-nouveau.html'

    def get_context_data(self, form=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = form if form else self.form_class()
        return context

    def post(self, request, **kwargs):
        context = super().get_context_data(**kwargs)
        form = self.form_class(request.POST)
        if not form.is_valid():
            return self.render_to_response(context, statut=400)
        #creation de l'apporteur
        try:
            apporteur = form.save()
        except Exception as e:
            _msg = 'une erreur (%s) est survenue lors de la création de apporteur %s' % (
                type(e).__name__, self.request.POST['nom'], e)
            messages.add_message(request, messages.ERROR, message=_msg)
            return self.render_to_response(context, statut=500)
        else:
            _msg= 'Apporteur %s créé avec succès' % apporteur.DenoSc
            messages.add_message(request, messages.INFO, message=_msg)
        return self.render_to_response(context, statut=201)


class ListApporteurView(TemplateView):
    template_name = 'apporteurs/apporteur-gestion.html'
    def get_context_data(self,*args, **kwargs):
        context = super(ListApporteurView, self).get_context_data(**kwargs)
        context['apporteurs'] = Apporteur.objects.all()
        return context

class EditApporteurView(TemplateView):
    template_name = 'apporteurs/apporteur-edit.html'
    form_class = ApporteurForm
    def get_context_data(self, form=None, *args, **kwargs):
        context = super(EditApporteurView, self).get_context_data(**kwargs)
        apporteur = get_object_or_404(Apporteur, pk=kwargs.get('pk'))
        context['form'] = form if form else self.form_class(instance=apporteur)
        return context
    def post(self, request, **kwargs):
        apporteur = get_object_or_404(Apporteur, pk=kwargs.get('pk'))
        form = self.form_class(request.POST, instance=apporteur)
        if not form.is_valid():
            context = self.get_context_data(form= form, **kwargs)
            return self.render_to_response(context, status=400)
        try:
            apporteur = form.save()
        except Exception as e:
            _msg = 'une erreur (%s) est survenue lors de la modification de apporteur %s: %s' % (
                type(e).__name__, self.request.POST['label'], e)
            messages.add_message(request, messages.ERROR, messages=_msg)
            context = self.get_context_data(form=form, **kwargs)
            return self.render_to_response(context, status=500)
        else:
            _msg = 'Apporteur %s modif avec succes' % apporteur.DenoSc
            messages.add_message(request, messages.INFO, message=_msg)
        context = self.get_context_data(**kwargs)
        return self.render_to_response(context, status=200)
