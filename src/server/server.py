import http
import sys, signal
from http.server import BaseHTTPRequestHandler
import socketserver
import url

# Cartella contente tutti i media della pagina, non vengono effettuati controlli
MEDIA = "/media"

# Legge il numero della porta dalla riga di comando
if sys.argv[1:]:
    port = int(sys.argv[1])
else:
    port = 8080


class Handler(http.server.SimpleHTTPRequestHandler):

    def do_AUTHHEAD(self):
        self.send_response(401)
        self.send_header('WWW-Authenticate', 'Basic realm=\"Test\"')
        self.send_header('Content-type', 'text/html')

        self.end_headers()

    def html(self):
        sub_path = self.path[1:]
        page_found = False
        for url_name in url.urlpatterns:
            if url_name[0] == sub_path:
                page = open(url_name[1]).read()
                page = url_name[2](self, page)
                self.do_HEAD()
                if page is not None:
                    self.wfile.write(bytes(page, "utf8"))  # legge l'url e cerca nella cartella
                    page_found = True
                break

        if not page_found:
            self.do_HEAD()
            self.wfile.write(bytes("404", "utf8"))

    def media(self):
        http.server.SimpleHTTPRequestHandler.do_GET(self)

    def do_HEAD(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()

    def do_GET(self):
        print(self.headers)
        if self.path[:6] == MEDIA:
            self.media()
        else:
            self.html()

    def do_POST(self):
        sub_path = self.path[1:]
        for url_name in url.urlpatterns:
            if url_name[0] == sub_path:
                page = open(url_name[1]).read()
                page = url_name[2](self, page)
                self.do_HEAD()
                if page is not None:
                    self.wfile.write(bytes(page, "utf8")) 


server = socketserver.ThreadingTCPServer(('', port), Handler)

# Assicura che da tastiera usando la combinazione
# di tasti Ctrl-C termini in modo pulito tutti i thread generati
server.daemon_threads = True
# il Server acconsente al riutilizzo del socket anche se ancora non è stato
# rilasciato quello precedente, andandolo a sovrascrivere
server.allow_reuse_address = True


# definiamo una funzione per permetterci di uscire dal processo tramite Ctrl-C
def signal_handler(signal, frame):
    print('Exiting http server (Ctrl+C pressed)')
    try:
        if server:
            server.server_close()
    finally:
        sys.exit(0)


# interrompe l’esecuzione se da tastiera arriva la sequenza (CTRL + C)
signal.signal(signal.SIGINT, signal_handler)

# entra nel loop infinito
try:
    while True:
        server.serve_forever()
except KeyboardInterrupt:
    pass

server.server_close()
