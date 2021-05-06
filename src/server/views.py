import login.login_required as login


@login.login_required
def index(request):
    print(request.headers)



def login(request):
    pass


def main():
    pass

if __name__ == "__main__":
    main()
