#Konstruktor som skapar self av namn, password, email,name och även en variabel: activeInChat som ställs som False i början
class User:
    def __init__(self,username_,password_,email_,name_):
        self.username = username_
        self.password = password_
        self.email = email_
        self.name = name_
        self.activeInChat = False

#Jämnför om password och usernamn stämmer överens med de i konstruktorn
    def isTheUser(self,username_,password_):
        if password_ == self.password and username_ == self.username:
            return True
        else:
            return False
#Denna konstruktorn skapar en lista av users
class CollectionOfUsers:
    def __init__(self):
        self.list_of_users = []

#En funktion som appendar user till listan i konstruktorn
    def add_user(self,username_,password_,email_,name_):
        usernameExists = False

        #loopar igenom users i listan och ser ifall username redan finns
        for user in self.list_of_users:
            if user.username == username_:
                usernameExists = True
                break

        #om det finns: returnera False
        if usernameExists == True:
            return False

        #om inte: appenda hela user till listan
        else:
            user = User(username_,password_,email_,name_)
            self.list_of_users.append(user)
            return True

#Funktion som loopar igenom listan för att hitta rätt användare, gör så att variabeln i konstruktorn activeInChat blir True istället.
    def doesThisUserExistAndNotActive(self,username_,password_):
        for user in self.list_of_users:
            if user.isTheUser(username_,password_):
                if user.activeInChat == False:
                    user.activeInChat = True
                    return True
                else:
                    return False
        return False

#Funktion som loopar igenom listan för att hitta rätt användare, ändrar sedan användarens activeInChat i konstruktorn till False
    def inactiveUser(self,usernameToInactive):
        for user in self.list_of_users:
            if user.username == usernameToInactive:
                user.activeInChat = False

#Funktion som tar bort en user ifrån listan, loopar igenom listan efter insert username och tar en pop
    def remove_user(self,username_):
        for i in range(self.list_of_users):
            if self.list_of_users[i].username == username_:
                self.list_of_users.pop(i)
                return True
        return False

#Funktion som genom det inskrivna namnet returnerar användaren genom att loopa igenom listan
    def getUserObjByUsername(self,username_):
        for i in range(self.list_of_users):
            if self.list_of_users[i].username == username_:
                return self.list_of_users[i]

        return "non"

#Läser users ifrån en textfil
    def readUsersFromFile(self):

        #Här försöker vi öppna textfilen och splittar den. Om inte filen lyckas öppna: returna False
        try:
            file = open("users.txt",'r')
            allLines = file.read().split('\n')
            file.close()
        except:
            return False

        #Vi skapar en variable för att deklarera att det ska börja på 0
        index_of_current_line = 0

        #En oändlig loop som läser varje rad och ökar sedan oavstående varaibel med 1 för att hoppa ner en rad
        while True:
            #För varje sektion nedan så läser den username, password etc.
            username = allLines[index_of_current_line]
            index_of_current_line+=1
            if username == "":
                return True

            password = allLines[index_of_current_line]
            index_of_current_line += 1
            if password == "":
                return False

            email = allLines[index_of_current_line]
            index_of_current_line += 1
            if email == "":
                return False

            name = allLines[index_of_current_line]
            index_of_current_line += 1
            if name == "":
                return False

            emptyLine = allLines[index_of_current_line]
            index_of_current_line+=1
            if emptyLine != "":
                return False

            #Här kallar den på funktioen add_user och skickar information som vi läst ifrån filen
            self.add_user(username,password,email,name)

            #När vår variable index_of_current_line når samma längst som AllLines så returnerar vi True
            if index_of_current_line == len(allLines):
                return True

#Gör så att varje users kontent (namn, password etc.) i listan addas till en variabel.
# Sedan öppnar man en textfil och skriver in variabeln för varje user i listan
    def writeUsersToFile(self):
        allContent = ""

        #För varje user i vår listan så addas namn, password, email, name plus tom rad till variabel över
        for user in self.list_of_users:
            allContent+=user.username+"\n"
            allContent+=user.password+"\n"
            allContent+=user.email+"\n"
            allContent+=user.name+"\n"
            allContent+="\n"

        #Vi försöker öppna en fil och sedan adda variabel som vi deklarerade i början. Om vi inte lyckas: returna False
        try:
            file = open("users.txt",'w')
            file.write(allContent)
            file.close()
            return True
        except:
            return False
