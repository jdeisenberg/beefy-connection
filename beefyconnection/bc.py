import cherrypy
import sqlite3


class BeefyConnection (object):
    exposed = True

    @cherrypy.expose
    def index(self):
        return "Welcome to the Beefy Connection"

    def user(self):
        return 'This is the "page" content'


class BeefyUser(object):

    exposed = True

    def __init__(self, dbfile):
        self.conn = sqlite3.connect(dbfile)

    def GET(self):
        user = None

        return ('''\
User Info:

First name: {0}
Last Name: {1}
Email: {2}'''.format(user['first'], user['last'], user['email']))

    def POST(self, first, last, email):
        self.conn.execute(
            '''INSERT INTO person (last_name, first_name, email)
            VALUES (%s, %s, %s)''' % (last, first, email))

        return ('Created a new user: {1}, {0}: {2}'.format(last, first, email))


def main():
    cherrypy.quickstart(BeefyConnection)

if __name__ == '__main__':
    main()

