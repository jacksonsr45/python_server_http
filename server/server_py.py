import os
try:
    from SimpleHTTPServer import SimpleHTTPReqquestHandler \
                            as SimpleHTTPReqquestHandler
    from SocketServer import TCPServer as Server
except ImportError:
    from http.server import SimpleHTTPRequestHandler as Handler
    from http.server import HTTPServer as Server

from config import config as c


#Read port selected by the cloud for our application
PORT = int(os.getenv('PORT', c['port']))

#path defoult from BASE_DIR of system
folder = c['primary_folder']
path = c['system_name']
value = os.path.basename(path)
BASER_DIR = """{}/{}""".format(path, folder)


#Change current directory
os.chdir(BASER_DIR)
#Exemple https://localhost:8000
httpd = Server(("%s" %c['local_host'], PORT), Handler)
try:
    print("Start serving at port %i" % PORT)
    httpd.serve_forever()
except KeyboardInterrupt:
    httpd.server_close()


httpd.server_close()