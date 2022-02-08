from django.shortcuts import get_object_or_404
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

    def get_context_data(self, form=None, contact_formset=None, *args, **kwargs):
        context = super(CreateNavireView, self).get_context_data(**kwargs)
        context['form'] = form if form else self.form_class()
        context['contact_formset'] = contact_formset if contact_formset else formset_factory(form=self.sub_form_class,
                                                                                             extra=1)
        return context

    def post(self, request, **kwargs):
        executor = self.request.user
        _lp = '[%s] %s.post' % (executor, self.__class__.__name__)
        form = self.form_class(data=request.POST)
        ContactFormSet = modelformset_factory(model=Moteur, form=self.sub_form_class)
        contact_formset = ContactFormSet(request.POST)
        context = self.get_context_data(form=form, contact_formset=contact_formset, **kwargs)
        if not all([form.is_valid(), contact_formset.is_valid()]):
            return self.render_to_response(context, status=400)
        # créer le navire
        try:
            navire = form.save()
            try:
                moteurs = contact_formset.save()
                for moteur in moteurs:
                    try:
                        moteur.save()
                    except Exception as e:
                        logger.error('%s une erreur %s pendant la création du moteur: %s' % (_lp, type(e).__name__, e))
                        moteur.delete()
                        raise e
            except Exception as e:
                navire.delete()
                _msg = 'Une erreur (%s) est survenue lors de la création du moteur lié au navire : %s' % (type(e).__name__, e)
                logger.error('%s %s' % (_lp, _msg))
                messages.add_message(request, messages.ERROR, message=_msg)
                return self.render_to_response(context, status=500)
        except Exception as e:
            _msg = 'Une erreur (%s) est survenue lors de la création du navire : %s' % (type(e).__name__, e)
            logger.error('%s %s' % (_lp, _msg))
            messages.add_message(request, messages.ERROR, message=_msg)
            return self.render_to_response(context, status=500)
        else:
            _msg = 'Navire créé avec succès'
            logger.info('%s %s' % (_lp, _msg))
            messages.add_message(request, messages.INFO, message=_msg)
        return self.render_to_response(context, status=201)


class EditNavireView(TemplateView):
    template_name = 'gestion/navire-gestion.html'
    form_class = NavireForm
    permissions = ['purchase.change_brand']

    def get_context_data(self, form=None, *args, **kwargs):
        brand = get_object_or_404(Navire, pk=kwargs.get('pk'))
        context = super(EditNavireView, self).get_context_data(**kwargs)
        context['form'] = form if form else self.form_class(instance=brand)
        return context

    def post(self, request, **kwargs):
        executor = self.request.user
        brand = get_object_or_404(Navire, pk=kwargs.get('pk'))
        _lp = '[%s] %s.post' % (executor, self.__class__.__name__)
        request = super(EditNavireView, self).post(**kwargs)
        form = self.form_class(data=request.POST, instance=brand)
        if not form.is_valid():
            context = self.get_context_data(form=form, **kwargs)
            return self.render_to_response(context, status=400)
        # edit the brand
        try:
            brand = form.save()
        except Exception as e:
            _msg = 'Une erreur (%s) est survenue lors de la mise à jour de la marque: %s' % (type(e).__name__, e)
            logger.error('%s %s' % (_lp, _msg))
            messages.add_message(request, messages.ERROR, message=_msg)
        else:
            _msg = 'Marque %s mise à jour avec succès' % brand.label
            logger.info('%s %s' % (_lp, _msg))
            messages.add_message(request, messages.INFO, message=_msg)
        context = self.get_context_data(**kwargs)
        return self.render_to_response(context, status=200)


class ListNavireView(TemplateView):
    template_name = 'gestion/navire-gestion.html'
    permissions = ['gestion.vue_navire']

    def get_context_data(self, *args, **kwargs):
        context = super(ListNavireView, self).get_context_data(**kwargs)
        context['navires'] = Navire.objects.all()
        return context


class CreateMoteurView(TemplateView):
    form_class = MoteurForm
    permissions = ['gestion.ajout_moteur']

    def get_context_data(self, form=None, *args, **kwargs):
        context = super(CreateMoteurView, self).get_context_data(**kwargs)
        context['form'] = form if form else self.form_class()
        return context

    def post(self, request, **kwargs):
        executor = self.request.user
        _lp = '[%s] %s.post' % (executor, self.__class__.__name__)
        context = self.get_context_data(**kwargs)
        form = self.form_class(request.POST)
        if not form.is_valid():
            context['form'] = form
            return self.render_to_response(context, status=400)
        # create the brand
        try:
            moteur = form.save()
        except Exception as e:
            _msg = 'Une erreur (%s) est survenue lors de la création du moteur: %s' % (type(e).__name__, e)
            logger.error('%s %s' % (_lp, _msg))
            messages.add_message(request, messages.ERROR, message=_msg)
        else:
            _msg = 'Moteur %s créé avec succès' % moteur.nom
            logger.info('%s %s' % (_lp, _msg))
            messages.add_message(request, messages.INFO, message=_msg)
        return self.render_to_response(context, status=201)

