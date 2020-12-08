#!/usr/bin/python3
import os
import threading
import http.server
from prometheus_client import start_http_server, Info

from http.server import HTTPServer, SimpleHTTPRequestHandler, BaseHTTPRequestHandler

i = Info('build_version', 'Version info')
i.info({'version': '1.2.3', 'maintainer': 'ronald.van.butselaar@trivento.nl'})

class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        if self.path == "/health":
            self.send_response(200)
            self.end_headers()
            self.wfile.write(b"OK")
        elif self.path == "/cpuleak":
            while True:
                with open('small_file.txt', 'r') as f:
                    for line in f:
                        giant_string = ''
                        giant_string+=line
        elif self.path == "/memoryleak":
            giant_string = ''
            while True:
                with open('small_file.txt', 'r') as f:
                    for line in f:
                        giant_string+=line
        else:
            self.send_response(200)
            self.end_headers()
            self.wfile.write("Hello {} \n".format(os.environ.get('NAME', 'world!')).encode('utf-8'))

if __name__ == '__main__':
    start_http_server(8000)

    server = http.server.ThreadingHTTPServer(('', 8080), SimpleHTTPRequestHandler)
    thread = threading.Thread(target = server.serve_forever)
    thread.start()
