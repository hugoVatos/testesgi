import importlib
import logging

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
