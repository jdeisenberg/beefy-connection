#import sqlite3
import ConfigParser

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



class BeefyConnection (object):
    exposed = True

    @cherrypy.expose
    def index(self):
        return "Welcome to the Beefy Connection"

    def user(self):
        return 'This is the "page" content'

class BeefyInterests(object):

    exposed = True

    def GET(self):
        return ('happy happy joy joy')

class BeefyUser(object):

    exposed = True

    def GET(self):
        user = None

        return ('''\
User Info:

First name: {0}
Last Name: {1}
Email: {2}'''.format(user['first'], user['last'], user['email']))

    def POST(self, first, last, email):
#        self.conn.execute(
#            '''INSERT INTO person (last_name, first_name, email)
#            VALUES (%s, %s, %s)''' % (last, first, email))
        return 'boomshaka'
#        return ('Created a new user: {1}, {0}: {2}'.format(last, first, email))

