from functools import wraps


def basic_access_authentication(funzione):
    @wraps(funzione)
    def wrapper(*args, **kwargs):

        if args[0].headers.get('Authorization') is None:
            args[0].do_AUTHHEAD()
            pass
        elif args[0].headers.get('Authorization') == 'Basic Y2lhbzpjaWFv':
            return funzione(*args, **kwargs)
        else:
            args[0].do_AUTHHEAD()
            pass

    return wrapper


def login_required(funzione):
    def wrapper(*args, **kwargs):

        if args[0].headers.get('Cookie') is None or args[0].headers.get('Cookie') != "pass=b'uname=ciao&psw=ciao'":
            args[0].send_response(301)
            args[0].send_header('Location', 'login')
            args[0].end_headers()

        else:
            return funzione(*args, **kwargs)


    return wrapper
