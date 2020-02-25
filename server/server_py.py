import os
try:
    from SimpleHTTPServer import SimpleHTTPReqquestHandler \
                            as SimpleHTTPReqquestHandler
    from SocketServer import TCPServer as Server
except ImportError:
    from http.server import SimpleHTTPRequestHandler as Handler
    from http.server import HTTPServer as Server



#Read port selected by the cloud for our application
PORT = int(os.getenv('PORT', 8000))

#path defoult from BASE_DIR of system
folder = 'static'
path = 'server'
value = os.path.basename(path)
BASER_DIR = """{}/{}""".format(path, folder)


#Change current directory
os.chdir(BASER_DIR)
httpd = Server(("", PORT), Handler)
try:
    print("Start serving at port %i" % PORT)
    httpd.serve_forever()
except KeyboardInterrupt:
    httpd.server_close()


httpd.server_close()