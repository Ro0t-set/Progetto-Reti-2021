import base64
import random
from src.server.login.login_request import basic_access_authentication, login_required
from src.server.login.password_validator import cookie_pwd_validator

def get_username(request):
    if request.headers.get('Authorization') is not None:
        return str(base64.b64decode(request.headers.get('Authorization').split(' ')[1])).split(':')[0][2:] + \
               """
        <a href="http://{rand_user}:{rand_pass}@{host}/logout">LogOut</a>
        """.format(host=request.headers.get('Host'), rand_user=random.randint(-1000, 1000),
                   rand_pass=random.randint(-1000, 1000))
    else:
        return "no logged"


def index(request, page):
    return page.format(username=get_username(request))


def info(request, page):
    return page.format(username=get_username(request))


def ambulatori(request, page):
    return page.format(username=get_username(request))


@basic_access_authentication
def referti(request, page):
    return page.format(username=get_username(request))


@basic_access_authentication
def turni(request, page):
    return page.format(username=get_username(request))


@login_required
def appuntamenti(request, page):
    return page.format(username=get_username(request))


def login(request, page):
    if "POST" in request.requestline:
        content_length = int(request.headers['Content-Length'])  # <--- Gets the size of data
        post_data = request.rfile.read(content_length)  # <--- Gets the data itself
        if cookie_pwd_validator("pass="+str(post_data)):
            request.send_response(301)
            request.send_header("Set-Cookie", "pass="+str(post_data))
            request.send_header('Location', '/')
            request.end_headers()
        else:
            request.send_response(301)
            request.send_header('Location', 'login')
            request.end_headers()

    return page


def logout(request, page):
    request.send_response(301)
    request.send_header("Set-Cookie", "pass=")
    request.send_header('Location', '/')
    request.end_headers()
    return page
