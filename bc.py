import cherrypy

interests = {
    'Ambassador': 'Represents Fedora',
    'Packaging': 'Package Software to be included in Fedora',
}

user = {}


class BeefyUser:

    exposed = True

    def GET(self):

        return('User Info:\n\nFirst name: {0}\nLast Name: {1}\nEmail: {2}'.format(user['first'], user['last'], user['email']))

    def POST(self, first, last, email):

        user = {
            'first': first,
            'last': last,
            'email': email,
        }

        return ('Created a new user: {1}, {0}: {2}'.format(last, first, email))


if __name__ == '__main__':

    cherrypy.tree.mount(
        BeefyUser(), '/api/user',
        {'/':
            {'request.dispatch': cherrypy.dispatch.MethodDispatcher()}
        }
    )

    cherrypy.engine.start()
    cherrypy.engine.block()

