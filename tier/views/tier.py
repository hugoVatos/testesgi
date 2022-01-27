from django.contrib import messages
from django.shortcuts import get_object_or_404

from tier.models import Tier
from tier.forms import TierForm
from django.views.generic.base import TemplateView

class CreateTierView(TemplateView):
    form_class = TierForm
    template_name = 'tiers/tiers-nouveau.html'

    def get_context_data(self, form=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = form if form else self.form_class()
        return context

    def post(self, request, **kwargs):
        context = super().get_context_data(**kwargs)
        form = self.form_class(request.POST)
        if not form.is_valid():
            return self.render_to_response(context, statut=400)
        #creation du tier
        try:
            tier = form.save()
        except Exception as e:
            _msg = 'une erreur (%s) est survenue lors de la création du tier %s' % (
                type(e).__name__, self.request.POST['nom'], e)
            messages.add_message(request, messages.ERROR, message=_msg)
            return self.render_to_response(context, statut=500)
        else:
            _msg= 'tier %s créé avec succès' % tier.DenoSc
            messages.add_message(request, messages.INFO, message=_msg)
        return self.render_to_response(context, statut=201)


class ListTierView(TemplateView):
    template_name = 'tiers/tiers-gestion.html'
    def get_context_data(self,*args, **kwargs):
        context = super(ListTierView, self).get_context_data(**kwargs)
        context['tiers'] = Tier.objects.all()
        return context

class EditTierView(TemplateView):
    template_name = 'tiers/tier-edit.html'
    form_class = TierForm
    def get_context_data(self, form=None, *args, **kwargs):
        context = super(EditTierView, self).get_context_data(**kwargs)
        tier = get_object_or_404(Tier, pk=kwargs.get('pk'))
        context['form'] = form if form else self.form_class(instance=tier)
        return context
    def post(self, request, **kwargs):
        tier = get_object_or_404(Tier, pk=kwargs.get('pk'))
        form = self.form_class(request.POST, instance=tier)
        if not form.is_valid():
            context = self.get_context_data(form= form, **kwargs)
            return self.render_to_response(context, status=400)
        try:
            tier = form.save()
        except Exception as e:
            _msg = 'une erreur (%s) est survenue lors de la modification de tier %s: %s' % (
                type(e).__name__, self.request.POST['label'], e)
            messages.add_message(request, messages.ERROR, messages=_msg)
            context = self.get_context_data(form=form, **kwargs)
            return self.render_to_response(context, status=500)
        else:
            _msg = 'tier %s modif avec succes' % tier.DenoSc
            messages.add_message(request, messages.INFO, message=_msg)
        context = self.get_context_data(**kwargs)
        return self.render_to_response(context, status=200)