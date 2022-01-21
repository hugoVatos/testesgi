from django.contrib import messages
from interlocuteur.models import Interlocuteur
from interlocuteur.forms import InterlocuteurForm
from django.views.generic.base import TemplateView

class CreateInterlocuteurView(TemplateView):
    form_class = InterlocuteurForm
    template_name = '/apporteur-nouveau.html'

    def get_context_data(self, form=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = form if form else self.form_class()
        return context

    def post(self, request, **kwargs):
        context = super().get_context_data(**kwargs)
        form = self.form_class(request.POST)
        if not form.is_valid():
            return self.render_to_response(context, statut=400)
        #creation de l'interlocuteur
        try:
            apporteur = form.save()
        except Exception as e:
            _msg = 'une erreur (%s) est survenue lors de la création de interlocuteur %s' % (
                type(e).__name__, self.request.POST['nom'], e)
            messages.add_message(request, messages.ERROR, message=_msg)
            return self.render_to_response(context, statut=500)
        else:
            _msg= 'Interlocteur %s créé avec succès' % apporteur.LastName
            messages.add_message(request, messages.INFO, message=_msg)
        return self.render_to_response(context, statut=201)


class ListInterlocuteurView(TemplateView):
    template_name = 'apporteurs/apporteur-gestion.html'
    def get_context_data(self,*args, **kwargs):
        context = super(ListInterlocuteurView, self).get_context_data(**kwargs)
        context['interlocuteurs'] = Interlocuteur.objects.all()
        return context