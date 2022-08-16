''' 
Ale Gudiel - 19232
Proyecto 1 - Redes 
Uso de un protocolo existente (XMPP) para comunicar con un servidor de mensajes

Archivo main para ejecutar el programa y mostrar el UI al usuario
'''
import sys
import logging
from argparse import ArgumentParser
from client import Client

if __name__ == '__main__':
    # setup the command line arguments.
    parser = ArgumentParser()

    # output verbosity options.
    parser.add_argument("-q", "--quiet", help="set logging to ERROR",
                        action="store_const", dest="loglevel",
                        const=logging.ERROR, default=logging.INFO)
    parser.add_argument("-d", "--debug", help="set logging to DEBUG",
                        action="store_const", dest="loglevel",
                        const=logging.DEBUG, default=logging.INFO)
    parser.add_argument("-e", "--error", help="set logging to ERROR",
                        action="store_const", dest="loglevel",
                        const=logging.ERROR, default=logging.INFO)
    
    arg = parser.parse_args()
    logging.basicConfig(level=arg.loglevel, format='%(levelname)-8s %(message)s')

    # ask for the intended options
    option = int(input("----------------------------\n*     Welcome to Alumchat     *\n----------------------------\n1. Sign Up\n2. Log In\n>> Please, enter a choice number: "))
    
    # get username and password from user input
    jid = input(">> Enter your user ending with @alumchat.fun: ")
    passwd = input(">> Enter your password: ")

    # start the client with the given options
    cli = Client(jid, passwd, userOptionInit=option)
    cli['xep_0077'].force_registration = True
    cli.connect()
    cli.process(forever=False)
    sys.exit()