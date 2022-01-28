import logging

from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm, PasswordResetForm
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.views.generic import TemplateView

from gestion.forms import CreateUtilisateurForm, EditAccountForm
from core.models import User


logger = logging.getLogger('taffe')


class CreateUtilisateurView(TemplateView):
    template_name = 'gestion/utilisateur-nouveau.html'
    form_class = CreateUtilisateurForm
    permissions = ['gestion.add_user']

    def get_context_data(self, form=None, *args, **kwargs):
        context = super(CreateUtilisateurView, self).get_context_data(**kwargs)
        context['form'] = form if form else self.form_class()
        return context

    def post(self, request, **kwargs):
        executor = self.request.user
        _lp = '[%s] %s.post' % (executor, self.__class__.__name__)
        request = super(CreateUtilisateurView, self).post(**kwargs)
        context = self.get_context_data(**kwargs)
        form = self.form_class(request.POST, request.FILES)
        if not form.is_valid():
            context['form'] = form
            logger.debug('form errors: %s' % form.errors)
            return self.render_to_response(context, status=400)
        # create the user
        try:
            user_profile = form.save()
        except Exception as e:
            _msg = 'Une erreur (%s) est survenue lors de la création de l\'utilisateur : %s' % (type(e).__name__, e)
            logger.error('%s %s' % (_lp, _msg))
            messages.add_message(request, messages.ERROR,
                                 message="Une erreur est survenue lors de la création de l'utilisateur")
        else:
            _msg = 'Utilisateur %s (%s) crée avec succès' % (user_profile.user.username, user_profile.user.email)
            logger.info('%s %s' % (_lp, _msg))
            messages.add_message(request, messages.INFO, message="Utilisateur crée avec succès")
            try:
                send_init_password_mail(user_profile.user)
            except Exception as e:
                _msg = 'Une erreur (%s) est survenue lors de l\'envoi d\'email d\'initialisation de mot de passe : %s' % (
                    type(e).__name__, e)
                messages.add_message(request, messages.ERROR, message=_msg)
        return self.render_to_response(context, status=201)


class ListUserView(TemplateView):
    template_name = 'gestion/utilisateur-gestion.html'
    permissions = ['gestion.view_user']

    def get_context_data(self, *args, **kwargs):
        executor = self.request.user
        _lp = '[%s] %s.get_context_data' % (executor, self.__class__.__name__)
        context = super(ListUserView, self).get_context_data(**kwargs)
        users = User.objects.all()
        context['users'] = users
        return context


class EditUserView(TemplateView):
    template_name = 'gestion/utilisateur-nouveau.html'
    form_class = EditAccountForm
    form_change_password_class = PasswordChangeForm

    def get_context_data(self, form=None, *args, **kwargs):
        executor = self.request.user
        user = executor
        if kwargs.get('pk'):
            user = get_object_or_404(User, pk=kwargs.get('pk'))
        context = super(EditUserView, self).get_context_data(**kwargs)
        if hasattr(user, 'usercompany'):
            context['form'] = form if form else self.form_class(user=user, company=user.usercompany.company)
        else:
            context['form'] = form if form else self.form_class(user=user)
        context['password_form'] = self.form_change_password_class(user)
        return context

    def post(self, request, **kwargs):
        executor = self.request.user
        user = executor
        if kwargs.get('pk'):
            user = get_object_or_404(User, pk=kwargs.get('pk'))
        _lp = '[%s] %s.post' % (executor, self.__class__.__name__)
        if 'change-password-submit' in request.POST:
            password_form = self.form_change_password_class(user, request.POST)
            if password_form.is_valid():
                user = password_form.save()
                update_session_auth_hash(request, user)  # Important!
                _msg = 'Votre mot de passe a été mis à jour avec succès'
                messages.add_message(request, messages.INFO, message=_msg)
                context = self.get_context_data()
                return self.render_to_response(context, status=200)
            else:
                _msg = 'Une erreur est survenue lors de la mise à jour de votre mot de passe'
                messages.add_message(request, messages.ERROR, message=_msg)
                context = self.get_context_data()
                return self.render_to_response(context, status=400)
        if hasattr(user, 'usercompany'):
            form = self.form_class(data=request.POST, user=user, company=user.usercompany.company)
        else:
            form = self.form_class(data=request.POST, user=user)
        context = self.get_context_data(form=form, **kwargs)
        if not form.is_valid():
            return self.render_to_response(context, status=400)
        # edit the user
        try:
            user, company = form.save()
        except Exception as e:
            _msg = 'A %s error occurred while updating user %s: %s' % (type(e).__name__, self.request.POST['email'], e)
            logger.error('%s %s' % (_lp, _msg))
            messages.add_message(request, messages.ERROR, message=_msg)
        else:
            _msg = 'User %s (%s) updated successfully' % (user.email, user.email)
            logger.info('%s %s' % (_lp, _msg))
            messages.add_message(request, messages.INFO, message='Compte mis à jour avec succès')
        return self.render_to_response(context, status=200)


def password_reset_request(request):
    if request.method == "POST":
        password_reset_form = PasswordResetForm(request.POST)
        if password_reset_form.is_valid():
            data = password_reset_form.cleaned_data['email']
            associated_users = User.objects.get(email=data)
            if associated_users:
                try:
                    emailing.send_init_password_mail(associated_users)
                except Exception as e:
                    return HttpResponse('Une erreur (%s) est survenue: %s' % (type(e).__name__, e))
                return HttpResponseRedirect(reverse('password_reset_done'))
    password_reset_form = PasswordResetForm()
    return render(request=request, template_name="account/password_reset.html",
                  context={"password_reset_form": password_reset_form})
