import socket
import _thread
import sys
from Server.Users import CollectionOfUsers

class SocketHandler:
    def __init__(self):
        #skapar socket
        self.serverSocket= socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        self.users = CollectionOfUsers()
        self.users.readUsersFromFile()

    def setGuiHandler(self,guiHandler_):
        self.guiHandler = guiHandler_

#Function för Close knappen som stänger av hela
    def closeEveryThing(self):
        self.serverSocket.close() #stänger av server socket
        self.users.writeUsersToFile() #skriver in Useres i text fil
        sys.exit(0) #stänger av programmet med sys

#Skapar en function för att Starta Acceptering
    def startAccepting(self):
        #Lägger det i en While loop för att acepteraa flera clienter
        while True:
            #testar koden annars om det blir error så hoppar det av till except(pass)
            try:
                clientSocket, clientAddr = self.serverSocket.accept()
                self.list_of_unknown_clientSockets.append(clientSocket)
                self.list_of_unknown_clientAddr.append(clientAddr)
                self.startReceiverThread(clientSocket, clientAddr)

            except:
                pass
#Function
    def startToAcceptConnection(self,port):
        try:
            self.serverSocket.bind(('',int(port)))
        except:
            return "failed"
        #börjar lyssna
        self.serverSocket.listen()
        #skapar en lista för clients som kan logga en
        self.list_of_known_clientSockets = []
        #skapar en lista för client adress som kan logga in
        self.list_of_known_clientAddr = []
        #lista för clients som inte har inloggnings uppgifter
        self.list_of_unknown_clientSockets = []
        #lista för client adress som inte har inloggnings uppgifter
        self.list_of_unknown_clientAddr = []
        #startar trådet för att börja acceptera
        _thread.start_new_thread(self.startAccepting,())
        return "succeed"
#en function för att skicka texten och visa på clients chatt fönster
    def sendAndShowMsg(self, text):
        self.guiHandler.showMessage(text)
        for clientSock in self.list_of_known_clientSockets:
            clientSock.send(str.encode(text))
#starta trådet  som recievar
    def startReceiverThread(self, clientSocket, clientAddr):
        _thread.start_new_thread(self.startReceiving,(clientSocket,clientAddr,))

    def startReceiving(self,clientSocket, clientAddr):
        resultOfLogin = self.listenToUnknownClinet(clientSocket,clientAddr)

        if resultOfLogin !=False:
            username = resultOfLogin
            self.list_of_unknown_clientSockets.remove(clientSocket)
            self.list_of_unknown_clientAddr.remove(clientAddr)

            self.list_of_known_clientSockets.append(clientSocket)
            self.list_of_known_clientAddr.append(clientAddr)

            self.listenToknownClinet(clientSocket,clientAddr,username)

#
    def listenToUnknownClinet(self,clientSocket, clientAddr):
        while True:
            try:
                msg = clientSocket.recv(1024).decode()
            except:
                self.list_of_unknown_clientSockets.remove(clientSocket)
                self.list_of_unknown_clientAddr.remove(clientAddr)
                return False

            args = msg.split(' ')
            if len(args) == 3 and args[0] == "login":
                username = args[1]
                password = args[2]
                if self.users.doesThisUserExistAndNotActive(username,password):
                    clientSocket.send(str.encode("ok"))
                    self.sendAndShowMsg(username + " is connected")
                    return username
                else:
                    clientSocket.send(str.encode("not ok"))

            if len(args) >= 5 and args[0] == "register":
                username = args[1]
                password = args[2]
                email = args[3]
                name = ""
                for rest in args[4:]:
                    name += rest + " "
                if username != "" and password != "" and email != "" and name != "":
                    resultOfAdding = self.users.add_user(username,password,email,name)
                    if resultOfAdding == True:
                        clientSocket.send(str.encode("fine"))
                    else:
                        clientSocket.send(str.encode("not fine"))
                else:
                    clientSocket.send(str.encode("not fine"))

    def listenToknownClinet(self,clientSocket, clientAddr,username):
        while True:
            try:
                msg = clientSocket.recv(1024).decode()
                self.sendAndShowMsg(username + ": " + msg)
            except:
                self.list_of_known_clientSockets.remove(clientSocket)
                self.list_of_known_clientAddr.remove(clientAddr)
                self.sendAndShowMsg(username+" disconnected")
                self.users.inactiveUser(username)
                return
