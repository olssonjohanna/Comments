#importerar tkinter library smamt message Box.
import tkinter
import tkinter.messagebox

#Definiton for GUI handler class, which allows the creation of the actual interface fo the chat server.
#It also calls the main.py server function.
class GuiHandler:
    def __init__(self,socketHandler_):
        self.socketHandler = socketHandler_

    #creates a interface with label and an entry field.

    def getPort(self):
        rootToGetPort = tkinter.Tk()
        lab = tkinter.Label(rootToGetPort,text="port")
        lab.grid(row = 0, column = 0)

        entOfPort = tkinter.Entry(rootToGetPort)
        entOfPort.grid(row = 0, column = 1)

    #returns the inputed port number as blank from the start.
        self.portToReturn = ""

        # creates a verification point with a button functionality.
        # it also calls the main.py server function.
        def confirmPort():
            self.portToReturn = entOfPort.get()
            rootToGetPort.destroy()
        but = tkinter.Button(rootToGetPort,text="set port",command = confirmPort)
        but.grid(row = 1, column = 0)

        #closes the main port input window by calling destroy() function.
        rootToGetPort.mainloop()

        #returns port to compare with client/user port input.
        return self.portToReturn

#main server GUI root Interface is created with tkinter settings.
    def startMainGui(self):
        self.root = tkinter.Tk()

        #ChatWindow is created and defined.
        scroll = tkinter.Scrollbar(self.root)
        scroll.grid(row = 0, column = 1, sticky=tkinter.N+tkinter.S)
        self.chattContents = tkinter.Text(self.root, yscrollcommand  = scroll.set)
        self.chattContents.grid(row = 0,column = 0)
        self.chattContents.config(state=tkinter.DISABLED)
        scroll.config(command=self.chattContents.yview)


        self.entryOfUser = tkinter.Entry(self.root)
        self.entryOfUser.grid(row = 1,column = 0)

        #Enter and Close buttons are created, each calls a function.
        self.buttonToTrigg = tkinter.Button(self.root, text = "enter", command = self.sendMsgBySocketHandler)
        self.buttonToTrigg.grid(row = 1,column = 1)
        self.buttonToTrigg = tkinter.Button(self.root, text = "close", command = self.closeConnection)
        self.buttonToTrigg.grid(row = 2,column = 0)
        self.root.mainloop()

    #call sockethandler instrutor function above and send admi messages to each connected client/chat member.
    def sendMsgBySocketHandler(self):
        self.socketHandler.sendAndShowMsg("Admin: " + self.entryOfUser.get())

    #Calls sockethandler instrutor, closes the server.
    def closeConnection(self):
        self.socketHandler.closeEveryThing()

    #Starts main server GUI interface.
    def startGui(self):
        self.startMainGui()

    #displays messages from sever.
    def showMessage(self,text):
        self.chattContents.config(state = tkinter.NORMAL)
        self.chattContents.insert(tkinter.END,text+"\n")

    #shows warning messages upton incorrect port binding.
        self.chattContents.config(state = tkinter.DISABLED)
        self.entryOfUser.delete(0,tkinter.END)
    def showWarningMsg(self):
        tkinter.messagebox.showwarning(message="could not bind port")