import sqlite3
import ConfigParser

class BeefyConfig(object):

    def __init__(self, args):
        self.cfgs = {}
        self._load_config(args.config)
        self.config_override(args)

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

    def config_override(self, args):
        if args.database:
            self.cfgs['db']['path'] = args.database


class BeefyConnection (object):
    exposed = True

    def index(self):
        return "Welcome to the Beefy Connection"

    def user(self):
        return 'This is the "page" content'

class BeefyUser(object):

    exposed = True

    def POST(self, first, last, email):
        self.conn.execute(
            '''INSERT INTO person (last_name, first_name, email)
            VALUES (%s, %s, %s)''' % (last, first, email))
        return ('Created a new user: {1}, {0}: {2}'.format(last, first, email))

class BeefyPic(object):

    exposed = True

    def POST(self, image):
        return('pic uploaded')
