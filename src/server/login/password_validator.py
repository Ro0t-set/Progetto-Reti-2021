import base64

user = [
    ("username", "password"),
    ("admin", "administrator")
]


def base_pwd_validator(username_password):
    for i in user:
        encoding_user = str(base64.b64encode("{user}:{pwd}".format(user=i[0], pwd=i[1]).encode()))
        encoding_user = encoding_user[2:len(encoding_user) - 1]
        if "Basic " + str(encoding_user) == str(username_password):
            return True

    return False


def cookie_pwd_validator(username_password):
    for i in user:
        encoding_user = """pass=b'uname={user}&psw={pwd}'""".format(user=i[0], pwd=i[1])
        if encoding_user == username_password:
            return True

    return False
