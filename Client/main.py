from Client.GuiHandler import GuiHandler
from Client.SocketHandler import SocketHandler

#test

socketHandler = SocketHandler()
guiHandler = GuiHandler(socketHandler)
socketHandler.setGuiHandler(guiHandler)

ip,port = guiHandler.getIpAndPort()

resultOfConnection = socketHandler.connect(ip,port)
if resultOfConnection == "no connection":
    guiHandler.showWarningMsg()
else:
    guiHandler.startGui()