import base64


def index(request, page):
    username = str(base64.b64decode(request.headers.get('Authorization').split(' ')[1])).split(':')[0][2:]
    print(username)
    return page.format(username=username)


def login(request):
    pass
