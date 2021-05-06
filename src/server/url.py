import views

# url name, file, file function, login required

urlpatterns = [
    ("home", "html/index.html", views.index, True)
]
