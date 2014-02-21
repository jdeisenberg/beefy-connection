import cherrypy
import sqlite3

class BeefyConnection (object):

    @cherrypy.expose
    def index(self):
        return "Welcome to the Beefy Connection"

    def user(self):
        return 'This is the "page" content'
    page.exposed = True

class BeefyUser(object):

    exposed = True

    def __init__(self, dbfile):
        self.conn=sqlite3.connect(dbfile)

    def GET(self):

        return('User Info:\n\nFirst name: {0}\nLast Name: {1}\nEmail: {2}'.format(user['first'], user['last'], user['email']))

    def POST(self, first, last, email):

        user = {
            'first': first,
            'last': last,
            'email': email,
        }
        self.conn.execute('INSERT INTO person (last_name, first_name, email)
                           VALUES (%s, %s, %s)' % (last, first, email))

        return ('Created a new user: {1}, {0}: {2}'.format(last, first, email))

if __name__ == '__main__':
    cherrypy.quickstart(BeefyConnection)

