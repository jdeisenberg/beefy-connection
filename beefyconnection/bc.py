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

class BeefyDisplay (object):

    def index(self):
        template_data = BeefyConfig.cfgs['template']
        exposed = True
        from String import Template
        f = open ('./template/beefy.template','r')
        return Template(f.read(),dict())
    index.exposed = True

class BeefyUser(object):

    exposed = True

    def __init__(self, bc):
        self.conn = sqlite3.connect(bc.cfgs['db']['path'])

    def POST(self, first, last, email, organization='NULL', irc='NULL',
        phone='NULL', address='NULL', city='NULL', state='NULL', postal='NULL',
        language='NULL', other_interest='NULL', comments='NULL', interests=None):
        """Get user data object from form submission"""

        self.conn.execute(
            '''INSERT INTO person ({0}, {1}, {2}, {3}, {4}, {5}, {6}, {7}, {8},
               {9}, {10}, {11}, {12}, {13})'''.format(last, first, email,
               organization, irc, phone, address, city, state, postal, language,
               other_interest, comments))

        ## getuid here

        if (interests):
            interest_list = interests.split()
            for interest in interest_lists:
              self.conn.execute('INSERT INTO interests (uid, interest)')

        return ('Created a new user: {1}, {0}: {2}'.format(last, first, email))

class BeefyPic(object):

    exposed = True

    def POST(self, image):
        return('pic uploaded')
