from Client.GuiHandler import GuiHandler
from Client.SocketHandler import SocketHandler

#

socketHandler = SocketHandler()
guiHandler = GuiHandler(socketHandler)
socketHandler.setGuiHandler(guiHandler)

ip,port = guiHandler.getIpAndPort()

resultOfConnection = socketHandler.connect(ip,port)
if resultOfConnection == "no connection":
    guiHandler.showWarningMsg()
else:
    guiHandler.startGui()