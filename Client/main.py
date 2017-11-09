from Comments.Client.GuiHandler import GuiHandler
from Comments.Client.SocketHandler import SocketHandler

socketHandler = SocketHandler() #skapar ett objekt utav Client.SocketHandler som skapar en socket
guiHandler = GuiHandler(socketHandler)#skapar ett objekt utav Client.GuiHandler som tar in våran socket som ett argument
socketHandler.setGuiHandler(guiHandler)#skickar in vårat guiHandler objekt till ClientSocketHandler så den kan använda sig utav det

ip,port = guiHandler.getIpAndPort()#Tar ipn och porten ifrån våran Gui

resultOfConnection = socketHandler.connect(ip,port)#använder ipn och porten för att connecta våran socket till den addressen
if resultOfConnection == "no connection":
    guiHandler.showWarningMsg()#Ger ett varningsmeddelande om att servern är ej funnen/gick inte att connecta
else:
    guiHandler.startGui()#annars börjar huvudsGui