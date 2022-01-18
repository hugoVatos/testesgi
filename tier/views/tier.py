from django.contrib import messages
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