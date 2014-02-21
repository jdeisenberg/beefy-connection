import cherrypy
import sqlite3
import argparse
import ConfigParser

interests = {
    'Ambassador': 'Represents Fedora',
    'Packaging': 'Package Software to be included in Fedora',
}

class BeefyConfig(object):

    def __init__(self):
        self.cfgs = {}

    def _load_config(self, path):
        """Constructor for skein, will create self.cfgs and self.logger

        :param str path:
        """

        config = ConfigParser.SafeConfigParser()
        try:
            f = open(path)
            config.readfp(f)
            f.close()
        except ConfigParser.InterpolationSyntaxError as e:
            raise Error("Unable to parse configuration file properly: %s" % e)

        for section in config.sections():
            if not self.cfgs.has_key(section):
                self.cfgs[section] = {}

            for k, v in config.items(section):
                self.cfgs[section][k] = v

user = {}

class BeefyInterests(object):
    exposed = True

    def get_interests():
      return "User Interest Info"

class BeefyUser(object):

    exposed = True

    def get_user():
      return "User Info"

    def GET(self):

        return('User Info:\n\nFirst name: {0}\nLast Name: {1}\nEmail: {2}'.format(user['first'], user['last'], user['email']))

    def POST(self, first, last, email):

        user = {
            'first': first,
            'last': last,
            'email': email,
        }
#        self.conn.execute('INSERT INTO person (last_name, first_name, email)
#                           VALUES (%s, %s, %s)' % (last, first, email)')

        return ('Created a new user: {1}, {0}: {2}'.format(last, first, email))

if __name__ == '__main__':

    bc = BeefyConfig()
    bc._load_config('beefy-connection.conf')

    parser=argparse.ArgummentParser(description='Beefy Connection!!!')
    parser.add_argument('-c', '--config', dest='config',
                        default='beefy-connection.cfg')
    parser.add_argument('-d', '--database', dest='database')
    args = parser.parse_args()

    cherrypy.tree.mount(
        BeefyUser(), '/bc/user',
        {'/':
            {'request.dispatch': cherrypy.dispatch.MethodDispatcher()}
        },
    )
    cherrypy.tree.mount(
        BeefyInterests(), '/bc/interests',
        {'/':
            {'request.dispatch': cherrypy.dispatch.MethodDispatcher()}
        }
    )

    cherrypy.engine.start()
    cherrypy.engine.block()

