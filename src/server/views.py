import base64
import login.login_request as login


@login.login_required
def index(request, page):
    if request.headers.get('Authorization') is not None:
        username = str(base64.b64decode(request.headers.get('Authorization').split(' ')[1])).split(':')[0][2:]
    else:
        username = "no logged"
    print(username)
    return page.format(username=username)


def login(request):
    pass
