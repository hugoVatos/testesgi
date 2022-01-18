from django.contrib import messages
from assureur.models import Assureur
from assureur.forms import AssureurForm
from django.views.generic.base import TemplateView

class CreateAssureurView(TemplateView):
    form_class = AssureurForm
    template_name = 'assureurs/assureur-nouveau.html'

    def get_context_data(self, form=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = form if form else self.form_class()
        return context

    def post(self, request, **kwargs):
        context = super().get_context_data(**kwargs)
        form = self.form_class(request.POST)
        if not form.is_valid():
            return self.render_to_response(context, statut=400)
        #creation de l'assureur
        try:
            assureur = form.save()
        except Exception as e:
            _msg = 'une erreur (%s) est survenue lors de la création de assureur %s' % (
                type(e).__name__, self.request.POST['nom'], e)
            messages.add_message(request, messages.ERROR, message=_msg)
            return self.render_to_response(context, statut=500)
        else:
            _msg= 'assureur %s créé avec succès' % assureur.DenoSc
            messages.add_message(request, messages.INFO, message=_msg)
        return self.render_to_response(context, statut=201)


class ListAssureurView(TemplateView):
    template_name = 'assureurs/assureur-gestion.html'
    def get_context_data(self,*args, **kwargs):
        context = super(ListAssureurView, self).get_context_data(**kwargs)
        context['assureurs'] = Assureur.objects.all()
        return context