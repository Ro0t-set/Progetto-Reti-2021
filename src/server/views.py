import random
def index(request, page):
    return page.format(username= request.headers.get('Authorization').split(' ')[0])


def login(request):
    pass
