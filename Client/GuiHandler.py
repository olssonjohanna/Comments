import tkinter
import tkinter.messagebox

#
class GuiHandler:
    def __init__(self,socketHandler_):
        self.socketHandler = socketHandler_ #Tar in socketen för att kunna använda sig utav den vid skickande av meddelande

    def getIpAndPort(self): #Skapar en ruta som tar in en ip och port för att connecta till servern
        rootToGetIpAndPort = tkinter.Tk()
        #skapar labels och lägger dom på en grid
        lab1 = tkinter.Label(rootToGetIpAndPort,text="ip")
        lab1.grid(row = 0, column = 0)
        lab2 = tkinter.Label(rootToGetIpAndPort,text="port")
        lab2.grid(row = 1, column = 0)
        #skapar entries för att ta in ipn och porten ifrån användaren
        entOfIp = tkinter.Entry(rootToGetIpAndPort)
        entOfIp.grid(row = 0, column = 1)
        entOfPort = tkinter.Entry(rootToGetIpAndPort)
        entOfPort.grid(row = 1, column = 1)

        self.ipAndPortToReturn = "",""#skapar ett return värde för den klass/funktion som kommer kalla på den här
        #funktionen för att skapa connection med användar input

        def confirmPortAndIpd():#en funktion för att skapa variablar som tar in de värden som är på entrieserna
            ip = entOfIp.get()
            port = entOfPort.get()
            self.ipAndPortToReturn = ip,port
            rootToGetIpAndPort.destroy()#dödar den ruta som frågar efter ip och port

        #skapar en knapp som hänvisar till funktionen "confirmPortAndIpd" och startar en mainloop på rutan
        but = tkinter.Button(rootToGetIpAndPort,text="set ip and port",command = confirmPortAndIpd)
        but.grid(row = 2, column = 0)
        rootToGetIpAndPort.mainloop()

        #returneran våran return variable
        return self.ipAndPortToReturn

    def startMainGui(self):
        #skapar chattrutan
        self.root = tkinter.Tk()
        #skapar en scrollbar
        scroll = tkinter.Scrollbar(self.root)
        scroll.grid(row = 0, column = 1, sticky=tkinter.N+tkinter.S)
        #rutan för att visa chatt texten och gör den read-only
        self.chattContents = tkinter.Text(self.root, yscrollcommand  = scroll.set)
        self.chattContents.grid(row = 0,column = 0)
        self.chattContents.config(state=tkinter.DISABLED)
        scroll.config(command=self.chattContents.yview)
        #skapar en entry/button för att skicka ett meddelande. buttonen hänvisar till våran funktion som skickar meddelandet.
        self.entryOfUser = tkinter.Entry(self.root)
        self.entryOfUser.grid(row = 1,column = 0)
        self.buttonToTrigg = tkinter.Button(self.root, text = "enter", command = self.sendMsgBySocketHandler)
        self.buttonToTrigg.grid(row = 1,column = 1)

        self.root.mainloop()#startar en mainloop på chattrutan

    def sendMsgBySocketHandler(self):#funktion som använder sig utav den socket som har tagits in vid skapandet av den här klassen.
        #den skickar entrien som usern har skrivit via våran socket.
        self.socketHandler.sendMsg(self.entryOfUser.get())

    def startIntroGui(self):#En ruta för att logga in och registerera en användare
        self.choiceRoot = tkinter.Tk()
        #skapar två knappar. En för att logga in som hänvisar till den här klassens function "funcToLogin" och den andra knappen "funcToRegister"
        but1 = tkinter.Button(self.choiceRoot, text ="log in", command = self.funcToLogin)
        but1.pack()
        but1 = tkinter.Button(self.choiceRoot, text ="register", command = self.funcToRegister)
        but1.pack()
        self.choiceRoot.mainloop()#startar en mainloop på inloggningsrutan

    def funcToLogin(self):#funktionen för att logga in
        self.loginChild = tkinter.Toplevel(self.choiceRoot)#skapar en ruta ovanpå våran "startIntroGui" ruta.
        #frågar användaren efter sitt användarnamn och lösenord
        lab1 = tkinter.Label(self.loginChild,text = "username")
        lab1.grid(row = 0, column = 0)
        lab2 = tkinter.Label(self.loginChild, text="password")
        lab2.grid(row=1, column=0)
        #skapar entries för användaren att skriva in sitt användarnamn cch lösenord
        entryOfUsername = tkinter.Entry(self.loginChild)
        entryOfUsername.grid(row=0, column=1)
        entryOfPassword = tkinter.Entry(self.loginChild)
        entryOfPassword.grid(row=1, column=1)

        def confirmLogin():#en subfunktion som skickar ett meddelande till klientens SocketHandler som i sin tur skickar till
            #serverns sockethandler som kollar om det finns en användare med det usernamet och passwordet eller om den användaren
            #är redan inloggad.
            username = entryOfUsername.get()
            password = entryOfPassword.get()
            self.socketHandler.sendMsg("login " + username + " " + password)
            self.loginChild.destroy()#dödar login rutan

        #knapp som hänvisar till "confirmLogin" funktionen
        but = tkinter.Button(self.loginChild,text = "log in", command = confirmLogin)
        but.grid(row = 2, column = 0)

    def funcToRegister(self):#funktionen för att registera
        self.registerChild = tkinter.Toplevel(self.choiceRoot)#skapar en ruta ovanpå våran "startIntroGui" ruta
        #Labels som beskriver entrieserna; username, password, email och name
        lab1 = tkinter.Label(self.registerChild,text = "username")
        lab1.grid(row = 0, column = 0)
        lab2 = tkinter.Label(self.registerChild, text="password")
        lab2.grid(row=1, column=0)
        lab3 = tkinter.Label(self.registerChild,text = "email")
        lab3.grid(row = 2, column = 0)
        lab4 = tkinter.Label(self.registerChild, text="name")
        lab4.grid(row=3, column=0)
        #entries för att skriva in infon
        entryOfUsername = tkinter.Entry(self.registerChild)
        entryOfUsername.grid(row=0, column=1)
        entryOfPassword = tkinter.Entry(self.registerChild)
        entryOfPassword.grid(row=1, column=1)
        entryOfEmail = tkinter.Entry(self.registerChild)
        entryOfEmail.grid(row=2, column=1)
        entryOfName = tkinter.Entry(self.registerChild)
        entryOfName.grid(row=3, column=1)

        def confirmRegister():#denna funktion skickar in entriesernas värde till ClientSocketHandler som i sin tur
            #skickar till ServerSocketHandler som tar upp meddelandet och registrerar användaren
            #skapar variablar som antar entriesernas värde
            username = entryOfUsername.get()
            password = entryOfPassword.get()
            email = entryOfEmail.get()
            name = entryOfName.get()
            self.socketHandler.sendMsg("register " + username + " " + password + " " + email + " " + name)#skickar meddelandet med våra entries
            self.registerChild.destroy()#dödar rutan

        but = tkinter.Button(self.registerChild,text = "register", command = confirmRegister)
        but.grid(row = 4, column = 0)

    def startGui(self):
        self.chattIsAllowed = False#kollar om man får chatta. om False så startas login och register rutan annars startas chattrutan
        self.startIntroGui()
        if self.chattIsAllowed == True:
            self.startMainGui()

    def showMessage(self,text):#Kollar om användaren får komma in i chattrutan
        if self.chattIsAllowed == False:
            if text == "ok": #om den text som returneras är "ok" får användaren komma in i chattrutan
                self.chattIsAllowed = True
                self.choiceRoot.destroy()#dödar login/register rutan
            elif text == "fine":
                tkinter.messagebox.showinfo(message="register is passed")#om den returnerade texten är "fine" gick det att registrera användaren
            elif text == "not ok":
                tkinter.messagebox.showinfo(message="log in failed")#om texten är "not ok" gick det inte att logga in
            elif text == "not fine":
                tkinter.messagebox.showinfo(message="register is failed")#om texten är "not fine" gick det inte att registrera
        else:
            self.chattContents.config(state = tkinter.NORMAL)#gör så att chattContents rutan kan skrivas till
            self.chattContents.insert(tkinter.END,text+"\n")#lägger in meddelandet
            self.chattContents.config(state = tkinter.DISABLED)#gör den till read-only
            self.entryOfUser.delete(0,tkinter.END)#rensar user entrien

    def showWarningMsg(self):
        tkinter.messagebox.showwarning(message="server is not found")#varning meddelande om servern ej är funnen#