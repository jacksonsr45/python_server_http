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



#Change current directory
os.chdir('static')
httpd = Server(("", PORT), Handler)
try:
    print("Start serving at port %i" % PORT)
    httpd.serve_forever()
except KeyboardInterrupt:
    pass


httpd.server_close()