#!/usr/bin/python3
import os
from http.server import BaseHTTPRequestHandler, HTTPServer

class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        self.wfile.write("Hello {} \n".format(os.environ.get('NAME', 'world!')).encode('utf-8'))


httpd = HTTPServer(('', 8080), SimpleHTTPRequestHandler)
httpd.serve_forever()
