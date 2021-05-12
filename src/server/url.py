import views
# 1) url da inserire nel sito
# 2) Percorso del file
# 3) Funzione associata al file
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
