from django.contrib import messages
from django.core.exceptions import BadRequest
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.views import View

from core.utils import class_for_name
from django.views.generic import TemplateView


class DeleteObjectView(TemplateView):
    permissions = []

    def get(self, request, *args, **kwargs):
        return_url = request.GET.get('return_url')
        module_name = request.GET.get('module_name')
        class_name = request.GET.get('class_name')
        if not return_url:
            raise BadRequest()
        if not module_name:
            messages.add_message(request, messages.ERROR, message='Veuillez renseigner le paramètre "module_name" dans l\'url')
        if not class_name:
            messages.add_message(request, messages.ERROR, message='Veuillez renseigner le paramètre "class_name" dans l\'url')
            return HttpResponseRedirect(redirect_to=return_url)

        instance = get_object_or_404(class_for_name('%s.models' % module_name, class_name), pk=kwargs.get('pk'))
        try:
            instance.delete()
            messages.add_message(request, messages.INFO, message='Suppression effectuée avec succès')
        except Exception as e:
            messages.add_message(request, messages.ERROR,
                                 message='Erreur (%s) est survenue lors de la suppression %s' % (type(e).__name__, e))
        return HttpResponseRedirect(redirect_to=return_url)
