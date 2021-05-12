import base64
from src.server.login.login_request import basic_access_authentication, login_required
from src.server.login.password_validator import cookie_pwd_validator


def get_username(request):
    log_string = ""
    # controlla se sono autenticato con "basic access authentication"
    if request.headers.get('Authorization') is not None:
        log_string = str(base64.b64decode(request.headers.get('Authorization').split(' ')[1])).split(':')[0][2:] + \
                     """
        <p>-> non e' possibile fare il logOut di questo protocollo</p>
        """
    # controlla se sono autenticato con i cookies
    if request.headers.get('Cookie') is not None or request.headers.get('Cookie') != "pass=":
        log_string = log_string + "classic login : <a href='http://user:pas@{host}/logout'>LogOut</a>".format(
            host=request.headers.get('Host'))

    return log_string


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


@basic_access_authentication
def appuntamenti(request, page):
    return page.format(username=get_username(request))


def login(request, page):
    # se la request è di tipo post
    if "POST" in request.requestline:
        content_length = int(request.headers['Content-Length'])  # <--- Gets the size of data
        post_data = request.rfile.read(content_length)  # <--- Gets the data itself
        # se la password è corretta
        if cookie_pwd_validator("pass=" + str(post_data)):
            # imposta i cookies
            request.send_response(301)
            request.send_header("Set-Cookie", "pass=" + str(post_data))
            request.send_header('Location', "/")
            request.end_headers()
            return None
        else:
            # se la password non è corretta
            page = page.format(login_state="username o password errati")
    else:
        # se la richiesta non è POST, presumibilmente GET
        page = page.format(login_state="inserire username e password")

    return page


def logout(request, page):
    # Imposta dei cookie privi di sognificato per forzare il logout
    request.send_response(301)
    request.send_header("Set-Cookie", "pass=")
    return page
