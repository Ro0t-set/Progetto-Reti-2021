from functools import wraps


def login_required(funzione):
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
