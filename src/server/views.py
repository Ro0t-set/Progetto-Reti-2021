import base64
import login.login_request as login


def get_username(request):
    if request.headers.get('Authorization') is not None:
        return str(base64.b64decode(request.headers.get('Authorization').split(' ')[1])).split(':')[0][2:] + \
               """
        <a href="http://username:password@localhost:8080">LogOut</a>
        """
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

def info_pdf(request, file):
    request.send_response(200)
    request.send_header('Content-type', 'pdf')
    request.end_headers()
    with open(file, 'rb') as file:
        request.wfile.write(file.read())
