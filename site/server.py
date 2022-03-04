import os
import sys
from http.server import HTTPServer, CGIHTTPRequestHandler

web_dir = './'
port = 80
if len(sys.argv) > 1: web_dir = sys.argv[1]
if len(sys.argv) > 2: port = int(sys.argv[2])
print('webdir "%s", port %s' % (web_dir, port))
os.chdir(web_dir)
server_address = ('', port)
server = HTTPServer(server_address, CGIHTTPRequestHandler)
server.serve_forever()  # обслуживать клиентов до завершения
