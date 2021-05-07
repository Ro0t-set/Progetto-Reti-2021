import base64
import login.login_request as login
import random


def get_username(request):
    if request.headers.get('Authorization') is not None:
        return str(base64.b64decode(request.headers.get('Authorization').split(' ')[1])).split(':')[0][2:] + \
               """
        <a href="http://{rand_user}:{rand_pass}@{host}">LogOut</a>
        """.format(host=request.headers.get('Host'), rand_user=random.randint(-1000, 1000), rand_pass=random.randint(-1000, 1000))
    else:
        return "no logged"


def index(request, page):
    return page.format(username=get_username(request))


def info(request, page):
    return page.format(username=get_username(request))


def ambulatori(request, page):
    return page.format(username=get_username(request))


@login.login_required
def referti(request, page):
    return page.format(username=get_username(request))


@login.login_required
def turni(request, page):
    return page.format(username=get_username(request))


@login.login_required
def appuntamenti(request, page):
    return page.format(username=get_username(request))
