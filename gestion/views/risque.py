from django.views.generic import TemplateView
from django.contrib import messages
from django.shortcuts import get_object_or_404

from core.utils import download
from gestion.models import Risque

from gestion.forms import RisqueForm


class CreateRisqueView(TemplateView):
    template_name = 'gestion/risque-nouveau.html'
    form_class = RisqueForm

    def get_context_data(self, form=None, *args, **kwargs):
        context = super(CreateRisqueView, self).get_context_data(**kwargs)
        context['form'] = form if form else self.form_class()
        return context

    def post(self, request, **kwargs):
        context = self.get_context_data(**kwargs)
        form = self.form_class(request.POST, request.FILES)

        if not form.is_valid():
            context['form'] = form
            return self.render_to_response(context, status=400)
        try:
            risque = form.save()
        except Exception as e:
            _msg = 'Une erreur (%s) est survenue lors de la création de la risque : %s' % (type(e).__name__, e)
            messages.add_message(request, messages.ERROR,
                                 message="Une erreur est survenue lors de la création du risque")
        else:
            _msg = 'Risque %s (%s) créee avec succès' % (risque.type, risque.intitule)
            messages.add_message(request, messages.INFO, message="Risque créee avec succès")
        return self.render_to_response(context, status=201)


class EditRisqueView(TemplateView):
    template_name = 'gestion/risque-modification.html'
    form_class = RisqueForm

    def get_context_data(self, form=None, *args, **kwargs):
        context = super(EditRisqueView, self).get_context_data(**kwargs)
        risque = get_object_or_404(Risque, pk=kwargs.get('pk'))
        context['form'] = form if form else self.form_class(instance=risque)
        return context

    def post(self, request, **kwargs):
        risque = get_object_or_404(Risque, pk=kwargs.get('pk'))
        form = self.form_class(request.POST, instance=risque)
        if not form.is_valid():
            context = self.get_context_data(form=form, **kwargs)
            return self.render_to_response(context, status=400)
        # edite la paie
        try:
            risque = form.save()
        except Exception as e:
            _msg = 'Une erreur (%s) est survenue lors de la modification du risque %s: %s' % (
                type(e).__name__, self.request.POST['label'], e)
            messages.add_message(request, messages.ERROR, message=_msg)
            context = self.get_context_data(form=form, **kwargs)
            return self.render_to_response(context, status=500)
        else:
            _msg = 'Risque de %s %s modifié avec succès' % (risque.type, risque.intitule)
            messages.add_message(request, messages.INFO, message=_msg)
        context = self.get_context_data(**kwargs)
        return self.render_to_response(context, status=200)


def download_risque(request, pk):
    risque = Risque.objects.filter(pk=pk)[0]
    filename = risque.fiche_pdf
    name = str(filename).split('/')[-1]

    response = download(request, pk, filename, name)
    return response


class ListRisqueView(TemplateView):
    template_name = 'gestion/risque-gestion.html'

    def get_context_data(self, *args, **kwargs):
        context = super(ListRisqueView, self).get_context_data(**kwargs)
        context['risques'] = Risque.objects.all()

        return context
