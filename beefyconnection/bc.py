import sqlite3
import simplejson
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


class BeefyConnection (object):
    exposed = True

    def index(self):
        return "Welcome to the Beefy Connection"

    def user(self):
        return 'This is the "page" content'

class BeefyUser(object):

    exposed = True

    def POST(self, user_json):
        """Get user_data json object from form submission"""

        user_data = simplejson.loads(user_json)

        return ('User Data: {0}'.format(user_data))

class BeefyPic(object):

    exposed = True

    def POST(self, image):
        return('pic uploaded')
