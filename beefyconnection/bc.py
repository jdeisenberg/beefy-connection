import sqlite3
import simplejson
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

class BeefyDisplay (object):
	def index(self):
		template_data = BeefyConfig.cfgs['template']
		exposed = True
		from String import Template
		f = open ('./template/beefy.template','r')
		return Template(f.read(),dict())

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
