import base64
import random
from src.server.login.login_request import basic_access_authentication, login_required
from src.server.login.password_validator import cookie_pwd_validator


def get_username(request):
    login = ""
    if request.headers.get('Authorization') is not None:
        login =  str(base64.b64decode(request.headers.get('Authorization').split(' ')[1])).split(':')[0][2:] + \
               """
        <a href="http://user:pas@{host}">LogOut</a>
        """.format(host=request.headers.get('Host'))

    if request.headers.get('Cookie') is None or request.headers.get('Cookie') == "pass=":
        login = login + "classic login : <a href='http://{host}/logout'>LogOut</a>".format(
            host=request.headers.get('Host'))


    return login

@login_required
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
        if cookie_pwd_validator("pass=" + str(post_data)):
            request.send_response(301)
            request.send_header("Set-Cookie", "pass=" + str(post_data))
            request.send_header('Location', "/")
            request.end_headers()
            return None
        else:
            page = page.format(login_state="username o password errati")
    else:
        page = page.format(login_state="inserire username e password")

    return page


def logout(request, page):
    request.send_response(301)
    request.send_header("Set-Cookie", "pass=")
    request.send_header('Location', '/')
    request.end_headers()
    return page
