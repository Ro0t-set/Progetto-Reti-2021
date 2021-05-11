import views
urlpatterns = [
    ("", "html/index.html", views.index),
    ("login", "html/login.html", views.login),
    ("logout", "html/logout.html", views.logout),
    ("info", "html/info.html", views.info),
    ("ambulatori", "html/ambulatori.html", views.ambulatori),
    ("referti", "html/referti.html", views.referti),
    ("turni", "html/turni.html", views.turni),
    ("appuntamenti", "html/appuntamenti.html", views.appuntamenti),
]
