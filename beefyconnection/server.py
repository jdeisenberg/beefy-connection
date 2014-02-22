import cherrypy
import argparse

from bc import BeefyUser, BeefyPic, BeefyConfig, BeefyConnection


def main():
    parser=argparse.ArgumentParser(description='Beefy Connection!!!')
    parser.add_argument('-c', '--config', dest='config',
                        default='beefy-connection.cfg')
    parser.add_argument('-d', '--database', dest='database')
    args = parser.parse_args()
    bc_config=BeefyConfig(args)

    cherrypy.tree.mount(
        BeefyUser(), '/bc/submit',
        {'/':
            {'request.dispatch': cherrypy.dispatch.MethodDispatcher()}
        }
    )
    cherrypy.tree.mount(
        BeefyPic(), '/bc/pic',
        {'/':
            {'request.dispatch': cherrypy.dispatch.MethodDispatcher()}
        }
    )

    cherrypy.engine.start()
    cherrypy.engine.block()

    cherrypy.quickstart(BeefyConnection())

if __name__ == '__main__':
    main()

