import base64
import login.login_request as login


def get_username(request):
    if request.headers.get('Authorization') is not None:
        return str(base64.b64decode(request.headers.get('Authorization').split(' ')[1])).split(':')[0][2:]
    else:
        return "no logged"


def index(request, page):
    return page.format(username=get_username(request))


def info(request, page):
    return page.format(username=get_username(request))


def ambulatori(request, page):
    return page.format(username=get_username(request))


def referti(request, page):
    return page.format(username=get_username(request))


def turni(request, page):
    return page.format(username=get_username(request))


def appuntamenti(request, page):
    return page.format(username=get_username(request))
