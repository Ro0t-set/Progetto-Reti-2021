import views

# url name, file, file function, login required

urlpatterns = [
    ("", "html/index.html", views.index),
    ("info", "html/info.html", views.info),
    ("ambulatori", "html/ambulatori.html", views.ambulatori),
    ("referti", "html/referti.html", views.referti),
    ("turni", "html/turni.html", views.turni),
    ("appuntamenti", "html/appuntamenti.html", views.appuntamenti)

]
