import importlib
import logging

from django.contrib.auth.forms import PasswordResetForm
from django.http import HttpResponse, HttpResponseRedirect, StreamingHttpResponse
from django.shortcuts import render
from django.urls import reverse


from gestion.models.utilisateur import Utilisateur

logger = logging.getLogger('taffe')


def class_for_name(module_name, class_name):
    # load the module, will raise ImportError if module cannot be loaded
    m = importlib.import_module(module_name)
    # get the class, will raise AttributeError if class cannot be found
    c = getattr(m, class_name)
    return c


def create_user_account(email, first_name=None, last_name=None, password=None):
    _lp = 'create_user_account:'

    # check that given email is available for a user account
    try:
        _ = Utilisateur.objects.get(email=email)
    except Utilisateur.DoesNotExist:
        pass
    else:
        raise ValueError('Email already used')

    # create the User instance
    _user = Utilisateur(email=email, is_active=True)
    if first_name is not None:
        _user.first_name = first_name
    if last_name is not None:
        _user.last_name = last_name
    if password is not None:
        _user.password = password
    try:
        _user.save()
    except Exception as e:
        _err = 'An error occurred while creating user account for %s: %s' % (email, type(e).__name__)
        logger.error('%s %s: %s' % (_lp, _err, e))
        _user.delete()
        raise Exception(_err)
    return _user


def get_unique_username(username):
    """

    :param username:
    :type username: str
    :return:
    :rtype: str
    """

    # find a unique username
    _username = None
    _suffix = 0
    _usernameProposal = username

    while not _username:
        if not user_exists(_usernameProposal):
            _username = _usernameProposal
            break

        _suffix += 1
        _usernameProposal = username + str(_suffix)

    return _username


def user_exists(username):
    try:
        _ = Utilisateur.objects.get(username=username)
    except Utilisateur.DoesNotExist:
        return False
    else:
        return True


def password_reset_request(request):
    if request.method == "POST":
        password_reset_form = PasswordResetForm(request.POST)
        if password_reset_form.is_valid():
            data = password_reset_form.cleaned_data['email']
            associated_users = Utilisateur.objects.get(email=data)
            if associated_users:
                try:
                    pass
                    #emailing.send_init_password_mail(associated_users)
                except Exception as e:
                    return HttpResponse('Une erreur (%s) est survenue: %s' % (type(e).__name__, e))
                return HttpResponseRedirect(reverse('password_reset_done'))
    password_reset_form = PasswordResetForm()
    return render(request=request, template_name="account/password_reset.html",
                  context={"password_reset_form": password_reset_form})


def download(request, pk, filename, name):
    filelocal = 'media/' + str(filename)
    file = open(filelocal)

    def file_iterator(file_name, chunk_size=512):
        with open(file_name, 'rb') as f:
            while True:
                c = f.read(chunk_size)
                if c:
                    yield c
                else:
                    break

    response = StreamingHttpResponse(file_iterator(filelocal))
    response['Content-Type'] = 'application/octet-stream'
    response['Content-Disposition'] = 'attachment;filename="' + str(name) + '"'
    return response