from django.contrib import messages
from django.shortcuts import get_object_or_404
from django.views.generic import TemplateView

from gestion.forms import TaxeForm
from gestion.models import Taxe


class CreateTaxeView(TemplateView):
    form_class = TaxeForm
    template_name = 'gestion/taxe-nouveau.html'

    def get_context_data(self, form=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = form if form else self.form_class()
        return context

    def post(self, request, **kwargs):
        context = self.get_context_data(**kwargs)
        form = self.form_class(request.POST)
        if not form.is_valid():
            return self.render_to_response(context, status=400)
        # créer la taxe
        try:
            taxe = form.save()
        except Exception as e:
            _msg = 'Une erreur (%s) est survenue lors de la création de la taxe %s: %s' % (
                type(e).__name__, self.request.POST['nom'], e)
            messages.add_message(request, messages.ERROR, message=_msg)
            return self.render_to_response(context, status=500)
        else:
            _msg = 'Taxe %s créée avec succès' % taxe.intitule
            messages.add_message(request, messages.INFO, message=_msg)
        return self.render_to_response(context, status=201)


class EditTaxeView(TemplateView):
    template_name = 'gestion/taxe-modification.html'
    form_class = TaxeForm

    def get_context_data(self, form=None, *args, **kwargs):
        context = super(EditTaxeView, self).get_context_data(**kwargs)
        taxe = get_object_or_404(Taxe, pk=kwargs.get('pk'))
        context['form'] = form if form else self.form_class(instance=taxe)
        return context

    def post(self, request, **kwargs):
        taxe = get_object_or_404(Taxe, pk=kwargs.get('pk'))
        form = self.form_class(request.POST, instance=taxe)
        if not form.is_valid():
            context = self.get_context_data(form=form, **kwargs)
            return self.render_to_response(context, status=400)
        # edite la taxe
        try:
            taxe = form.save()
        except Exception as e:
            _msg = 'Une erreur (%s) est survenue lors de la modificaion de la taxe %s: %s' % (
                type(e).__name__, self.request.POST['label'], e)
            messages.add_message(request, messages.ERROR, message=_msg)
            context = self.get_context_data(form=form, **kwargs)
            return self.render_to_response(context, status=500)
        else:
            _msg = 'Taxe %s modifié avec succès' % taxe.intitule
            messages.add_message(request, messages.INFO, message=_msg)
        context = self.get_context_data(**kwargs)
        return self.render_to_response(context, status=200)


class ListTaxeView(TemplateView):
    template_name = 'gestion/taxe-gestion.html'

    def get_context_data(self, *args, **kwargs):
        context = super(ListTaxeView, self).get_context_data(**kwargs)
        context['taxes'] = Taxe.objects.all()
        return context
