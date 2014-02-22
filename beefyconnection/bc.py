import sqlite3
import argparse
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

class BeefyDisplay (object):
	def index(self):
		template_data = BeefyConfig.cfgs['template']
		exposed = True
		from String import Template
		f = open ('./template/beefy.template','r')
		return Template(f.read(),dict())

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

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Beefy Connection webserver!')
    parser.add_argument('-c', '--config', action='store',
            default='beefy-connection.conf')
    parser.add_argument('-d', '--database', action='store')
    args = parser.parse_args()
