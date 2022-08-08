# Ale Gudiel - 19232
# Archivo para registrar o eliminar usuarios del servidor alumnchat

#Importamos librerías útiles
import xmpp
import slixmpp
from slixmpp.exceptions import IqError, IqTimeout
from slixmpp.xmlstream.stanzabase import ET

# Definimos el registro de usuarios para el server alumnchay
def registerUser(user, passwrd):
    jid = xmpp.JID(user)
    cl = xmpp.Client(jid.getDomain(), debug=[])
    cl.connect()

    if xmpp.features.register(cl, jid.getDomain(), {'username': jid.getNode(), 'password': passwrd}):
        print("User succesfully registered!")
        return True
    else:
        print("User already registered!")
        return False

# Definimos la clase para eliminar usuarios del server alumnchat
class DeleteUser(slixmpp.ClientXMPP):
    def __init__(self, jid, passwrd, showUser, statusUser):
        slixmpp.ClientXMPP.__init__(self, jid, passwrd)
        self.user = jid
        self.showUser = showUser
        self.statusUser = statusUser
        self.add_event_handler("session_start", self.start)

    def startSession(self, event):
        self.send_presence()
        self.get_roster()
        self.deleteUser()

    def deleteUser(self):
        delete = self.Iq()
        delete['type'] = 'set'
        delete['from'] = self.user
        fragment = ET.fromstring("<query xmlns='jabber:iq:register'><remove/></query>")
        delete.append(fragment)

        try:
            delete.send()
            print("User succesfully deleted!")
            self.disconnect()
        except IqError as e:
            print("There was an error deleting the user: %s" % e.iq['error']['text'])
            self.disconnect()
