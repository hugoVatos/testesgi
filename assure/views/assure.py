from django.contrib import messages
from django.shortcuts import get_object_or_404

from assure.models import Assure
from assure.forms import AssureForm
from django.views.generic.base import TemplateView

class CreateAssureView(TemplateView):
    form_class = AssureForm
    template_name = 'assures/assure-nouveau.html'

    def get_context_data(self, form=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = form if form else self.form_class()
        return context

    def post(self, request, **kwargs):
        context = super().get_context_data(**kwargs)
        form = self.form_class(request.POST)
        if not form.is_valid():
            return self.render_to_response(context, statut=400)
        #creation de l'assuré
        try:
            assure = form.save()
        except Exception as e:
            _msg = 'une erreur (%s) est survenue lors de la création de assuré %s' % (
                type(e).__name__, self.request.POST['nom'], e)
            messages.add_message(request, messages.ERROR, message=_msg)
            return self.render_to_response(context, statut=500)
        else:
            _msg= 'assuré %s créé avec succès' % assure.DenoSc
            messages.add_message(request, messages.INFO, message=_msg)
        return self.render_to_response(context, statut=201)


class ListAssureView(TemplateView):
    template_name = 'assures/assure-gestion.html'
    def get_context_data(self,*args, **kwargs):
        context = super(ListAssureView, self).get_context_data(**kwargs)
        context['assures'] = Assure.objects.all()
        return context

class EditAssureView(TemplateView):
    template_name = 'assures/assure-edit.html'
    form_class = AssureForm
    def get_context_data(self, form=None, *args, **kwargs):
        context = super(EditAssureView, self).get_context_data(**kwargs)
        assure = get_object_or_404(Assure, pk=kwargs.get('pk'))
        context['form'] = form if form else self.form_class(instance=assure)
        return context
    def post(self, request, **kwargs):
        assure = get_object_or_404(Assure, pk=kwargs.get('pk'))
        form = self.form_class(request.POST, instance=assure)
        if not form.is_valid():
            context = self.get_context_data(form= form, **kwargs)
            return self.render_to_response(context, status=400)
        try:
            assure = form.save()
        except Exception as e:
            _msg = 'une erreur (%s) est survenue lors de la modification de assuré %s: %s' % (
                type(e).__name__, self.request.POST['label'], e)
            messages.add_message(request, messages.ERROR, messages=_msg)
            context = self.get_context_data(form=form, **kwargs)
            return self.render_to_response(context, status=500)
        else:
            _msg = 'assuré %s modif avec succes' % assure.DenoSc
            messages.add_message(request, messages.INFO, message=_msg)
        context = self.get_context_data(**kwargs)
        return self.render_to_response(context, status=200)