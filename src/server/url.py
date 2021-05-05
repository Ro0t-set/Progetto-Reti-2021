import views

# url name, file, file function

urlpatterns = [
    ("home", "html/index.html", views.index),
    ("login", "html/login.html", views.login)
]
