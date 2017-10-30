import socket
import _thread

#Vår konstruktor som skapar en client socket
class SocketHandler:
    def __init__(self):
        self.clientSocket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

#Skapar en self av inkommande variable: guihandler
    def setGuiHandler(self,guiHandler_):
        self.guiHandler = guiHandler_

#Denna funktion får IP och port. Försöker att connecta och vid sucess: sätter igång en funktion startRecieverThread. Om inte: return "no connection"
    def connect(self,ip, port):
        try:
            self.clientSocket.connect((ip,int(port)))
            self.startReceiverThread()
        except:
            return "no connection"

#En funktion som försöker att skicka meddelande till servern
    def sendMsg(self,text):
        try:
            self.clientSocket.send(str.encode(text))
        except:
            pass

#En funktion som skapar en tråd, som ska göra funktionen_ startRecieving
    def startReceiverThread(self):
        _thread.start_new_thread(self.startReceiving,())

#Funktionen tar emot oändligt med messages, vid mottagande så startar den funktionen: showMessage med det recv meddelandet vid except: visar den deconnected.
    def startReceiving(self):
        while True:
            try:
                msg = self.clientSocket.recv(1024).decode()
                self.guiHandler.showMessage(msg)
            except:
                self.guiHandler.showMessage("desconnected...")
                return