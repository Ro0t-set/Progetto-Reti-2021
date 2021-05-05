login_status = 0


def login_required(func):
    def wrapper():
        global login_status
        if login_status == 0:
            login_status = 1
        else:
            login_status = 0
        print(login_status)
        func()
    return wrapper


def main():
    pass


if __name__ == "__main__":
    main()
