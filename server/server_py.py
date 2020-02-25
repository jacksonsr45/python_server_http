import os
try:
    from SimpleHTTPServer import SimpleHTTPReqquestHandler \
                            as SimpleHTTPReqquestHandler
    from SocketServer import TCPServer as Server
except ImportError:
    from http.server import SimpleHTTPRequestHandler as Handler
    from http.server import HTTPServer as Server
from .config import config as c


class New_Server:
    def __init__(self):
        #Init variables 
        self.folder = c['primary_folder']
        self.path = c['system_name']
                
        #Read port selected by the cloud for our application
        PORT = int(os.getenv('PORT', c['port']))

        #Change current directory
        os.chdir(self.BASE_DIR( self.path, self.folder))     
        self.UP_SERVER(PORT)


    def BASE_DIR(self, path, folder):
        #path defoult from BASE_DIR of system
        value = os.path.basename(path)
        path_value = '%s' % value+'/'+'%s' % folder
        return path_value

    def UP_SERVER(self, PORT):
        #Exemple https://localhost:8000
        httpd = Server(("%s" %c['local_host'], PORT), Handler)
        try:
            print("Start serving at port %i" % PORT)
            httpd.serve_forever()
        except KeyboardInterrupt:
            httpd.server_close()

        httpd.server_close()