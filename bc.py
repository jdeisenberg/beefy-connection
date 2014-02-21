import cherrypy

class BeefyConnection (object):

    @cherrypy.expose
    def index(self):
        return "Welcome to the Beefy Connection"

    def user(self):
        return 'This is the "page" content'
    page.exposed = True


if __name__ == '__main__':
    cherrypy.quickstart(BeefyConnection)

