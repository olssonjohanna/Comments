from Server.GuiHandler import GuiHandler
from Server.SocketHandler import SocketHandler

socketHandler = SocketHandler()#skapar ett objekt utav Server.SocketHandler.
guiHandler = GuiHandler(socketHandler)#skapar ett objekt utav Client.GuiHandler som tar in våran socket som ett argument
socketHandler.setGuiHandler(guiHandler)#skickar in vårat guiHandler objekt till ServerSocketHandler så den kan använda sig utav det

port = guiHandler.getPort()#Tar porten som användaren skriver in
resultOfBinding = socketHandler.startToAcceptConnection(port)#skapar en variabel som testar binda sig till den port vi fick

if resultOfBinding == "failed":
    guiHandler.showWarningMsg()#skickar ett varningsmeddelande om det misslyckas
else:
    guiHandler.startGui()#startar gui

#new comment :)

