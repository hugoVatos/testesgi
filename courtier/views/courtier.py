from django.contrib import messages
from courtier.models import Courtier
from courtier.forms import CourtierForm
from django.views.generic.base import TemplateView

class CreateCourtierView(TemplateView):
    form_class = CourtierForm
    template_name = 'courtiers/courtier-nouveau.html'

    def get_context_data(self, form=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = form if form else self.form_class()
        return context

    def post(self, request, **kwargs):
        context = super().get_context_data(**kwargs)
        form = self.form_class(request.POST)
        if not form.is_valid():
            return self.render_to_response(context, statut=400)
        #creation du courtier
        try:
            courtier = form.save()
        except Exception as e:
            _msg = 'une erreur (%s) est survenue lors de la création du courtier %s' % (
                type(e).__name__, self.request.POST['nom'], e)
            messages.add_message(request, messages.ERROR, message=_msg)
            return self.render_to_response(context, statut=500)
        else:
            _msg= 'Courtier %s créé avec succès' % courtier.DenoSc
            messages.add_message(request, messages.INFO, message=_msg)
        return self.render_to_response(context, statut=201)


class ListCourtierView(TemplateView):
    template_name = 'courtiers/courtier-gestion.html'
    def get_context_data(self,*args, **kwargs):
        context = super(ListCourtierView, self).get_context_data(**kwargs)
        context['courtiers'] = Courtier.objects.all()
        return context