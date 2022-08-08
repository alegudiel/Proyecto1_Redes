# Ale Gudiel - 19232
# Archivo que contiene la clase Login para el manejo de la sesion de usuario

import xmpp
import slixmpp
import logging
from slixmpp.exceptions import IqError, IqTimeout

class Login(slixmpp.ClientXMPP):
    # Constructor de la clase Login
    # jid: JID del usuario
    def __init__(self, jid, password):
        slixmpp.ClientXMPP.__init__(self, jid, password)
        self.add_event_handler("session_start", self.start)
        self.add_event_handler("menuOptions", self.menuOptions)

    # Funcion que se ejecuta al iniciar la sesion del usuario
    def startSession(self, event):
        self.send_presence()
        self.get_roster()
        

    def menuOptions(self):
        pass
