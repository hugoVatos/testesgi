from django.contrib import messages
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