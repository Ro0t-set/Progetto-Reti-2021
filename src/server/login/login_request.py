from functools import wraps
import src.server.login.password_validator as pwd



def basic_access_authentication(funzione):
    @wraps(funzione)
    def wrapper(*args, **kwargs):

        if args[0].headers.get('Authorization') is None:
            args[0].do_AUTHHEAD()
            pass
        elif pwd.base_pwd_validator(args[0].headers.get('Authorization')):
            return funzione(*args, **kwargs)
        else:
            args[0].do_AUTHHEAD()
            pass

    return wrapper


def login_required(funzione):
    def wrapper(*args, **kwargs):
        if not pwd.cookie_pwd_validator(args[0].headers.get('Cookie')):
            args[0].send_response(301)
            args[0].send_header('Location', 'login')
            args[0].end_headers()

        else:
            return funzione(*args, **kwargs)

    return wrapper
