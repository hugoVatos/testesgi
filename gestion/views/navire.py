from django.shortcuts import get_object_or_404
from django.views import generic
from django.views.generic import TemplateView
import logging

from django.contrib import messages

from django.forms import modelformset_factory, formset_factory
from gestion.models import Navire, Moteur
from gestion.forms import NavireForm, MoteurForm

logger = logging.getLogger('taffe')


class CreateNavireView(TemplateView):
    template_name = 'gestion/navire-nouveau.html'
    permissions = ['gestion.ajout_navire']
    form_class = NavireForm
    sub_form_class = MoteurForm

    def get_context_data(self, form=None, moteur_formset=None, *args, **kwargs):
        context = super(CreateNavireView, self).get_context_data(**kwargs)
        context['form'] = form if form else self.form_class()
        context['moteur_formset'] = moteur_formset if moteur_formset else formset_factory(form=self.sub_form_class, extra=1)
        return context

    def post(self, request, **kwargs):
        executor = self.request.user
        _lp = '[%s] %s.post' % (executor, self.__class__.__name__)
        MoteurFormSet = modelformset_factory(model=Moteur, form=self.sub_form_class)
        form = self.form_class(request.POST)
        moteur_formset = MoteurFormSet(request.POST)
        context = self.get_context_data(form=form, moteur_formset=moteur_formset, **kwargs)
        for field in form:
            print("Field Error:", field.name, field.errors)
        print('Form navire valide : ' + str(form.is_valid()))
        print('Form moteur valide : ' + str(moteur_formset.is_valid()))

        if not all([form.is_valid(), moteur_formset.is_valid()]):
            return self.render_to_response(context, status=400)
        # créer le navire
        try:
            navire = form.save()
            try:
                #création du ou des moteurs associés
                moteurs = moteur_formset.save(commit=False)
                for moteur in moteurs:
                    moteur.navire = navire
                    moteur.save()
            except Exception as e:
                navire.delete()
                _msg = 'Une erreur (%s) est survenue lors de la création du moteur lié au navire : %s' % (type(e).__name__, e)
                logger.error('%s %s' % (_lp, _msg))
                print('Une erreur est survenue lors de la création du moteur lié au navire')
                messages.add_message(request, messages.ERROR, message=_msg)
                return self.render_to_response(context, status=500)
        except Exception as e:
            _msg = 'Une erreur (%s) est survenue lors de la création du navire : %s' % (type(e).__name__, e)
            logger.error('%s %s' % (_lp, _msg))
            print('Une erreur est survenue lors de la création du navire')
            messages.add_message(request, messages.ERROR, message=_msg)
            return self.render_to_response(context, status=500)
        else:
            _msg = 'Navire créé avec succès'
            logger.info('%s %s' % (_lp, _msg))
            messages.add_message(request, messages.INFO, message=_msg)
        return self.render_to_response(context, status=201)


class EditNavireView(TemplateView):
    template_name = 'gestion/navire-modification.html'
    form_class = NavireForm
    sub_form_class = MoteurForm
    permissions = ['gestion.modification_navire']

    def get_context_data(self, form=None, *args, **kwargs):
        context = super(EditNavireView, self).get_context_data(**kwargs)
        navire = get_object_or_404(Navire, pk=kwargs.get('pk'))
        context['form'] = form if form else self.form_class(instance=navire)
        MoteurFormSet = modelformset_factory(model=Moteur, form=self.sub_form_class, extra=0)
        context['moteur_formset'] = MoteurFormSet(queryset=navire.moteur_set.all())
        return context

    def post(self, request, **kwargs):
        executor = self.request.user
        _lp = '[%s] %s.post' % (executor, self.__class__.__name__)
        navire = get_object_or_404(Navire, pk=kwargs.get('pk'))
        MoteurFormSet = modelformset_factory(model=Moteur, form=self.sub_form_class, extra=0)
        form = self.form_class(data=request.POST, instance=navire)
        moteur_formset = MoteurFormSet(data=request.POST)
        if not all([form.is_valid(), moteur_formset.is_valid()]):
            context = self.get_context_data(form=form,moteur_formset=moteur_formset, **kwargs)
            return self.render_to_response(context, status=400)
        # edit the brand
        try:
            navire = form.save()
            moteur_formset.save()
        except Exception as e:
            _msg = 'Une erreur (%s) est survenue lors de la mise à jour de la marque: %s' % (type(e).__name__, e)
            logger.error('%s %s' % (_lp, _msg))
            messages.add_message(request, messages.ERROR, message=_msg)
        else:
            _msg = 'Marque %s mise à jour avec succès' % navire.label
            logger.info('%s %s' % (_lp, _msg))
            messages.add_message(request, messages.INFO, message=_msg)
        context = self.get_context_data(form=form, moteur_formset=moteur_formset, **kwargs)
        return self.render_to_response(context, status=200)


class ListNavireView(TemplateView):
    template_name = 'gestion/navire-gestion.html'
    permissions = ['gestion.vue_navire']

    def get_context_data(self, *args, **kwargs):
        context = super(ListNavireView, self).get_context_data(**kwargs)
        context['navires'] = Navire.objects.all()
        return context


