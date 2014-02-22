import cherrypy
import argparse

from bc import BeefyUser, BeefyInterests, BeefyConfig, BeefyConnection


def main():

    parser=argparse.ArgumentParser(description='Beefy Connection!!!')
    parser.add_argument('-c', '--config', dest='config',
                        default='beefy-connection.cfg')
    parser.add_argument('-d', '--database', dest='database')
    args = parser.parse_args()

    cherrypy.tree.mount(
        BeefyUser(), '/bc/user',
        {'/':
            {'request.dispatch': cherrypy.dispatch.MethodDispatcher()}
        }
    )
    cherrypy.tree.mount(
        BeefyInterests(), '/bc/interests',
        {'/':
            {'request.dispatch': cherrypy.dispatch.MethodDispatcher()}
        }
    )

    cherrypy.engine.start()
    cherrypy.engine.block()

    cherrypy.quickstart(BeefyConnection())

if __name__ == '__main__':
    main()

