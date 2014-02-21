import cherrypy
import sqlite3
import argparse

interests = {
    'Ambassador': 'Represents Fedora',
    'Packaging': 'Package Software to be included in Fedora',
}

user = {}

class BeefyInterests(object):
    exposed = True

    def get_interests():
      return "User Interest Info"

class BeefyUser(object):

    exposed = True

    def get_user():
      return "User Info"

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

    parser=argparse.ArgummentParser(description='Beefy Connection!!!')
    parser.add_argument('-c', '--config', dest='config',
                        default='beefy-connection.cfg')
    parser.add_argument('-d', '--database', dest='database')
    args = parser.parse_args()

    cherrypy.tree.mount(
        BeefyUser(), '/bc/user',
        {'/':
            {'request.dispatch': cherrypy.dispatch.MethodDispatcher()}
        }
        BeefyInterests(), '/bc/interests',
        {'/':
            {'request.dispatch': cherrypy.dispatch.MethodDispatcher()}
        }
    )

    cherrypy.engine.start()
    cherrypy.engine.block()

