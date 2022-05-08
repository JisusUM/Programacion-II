class userCrud:
    # Declaración del constructor
    def __init__(self, __dni:int, __name:str, __lastName:str, __gender:str, __phoneNumber:str, __emergencyContact:str,
                __emailAddress:str, __address:str):

        # Datos de entrada
        self.dni = __dni
        self.name = __name
        self.lastName = __lastName
        self.gender = __gender
        self.phoneNumber = __phoneNumber
  
      

#10539876534, "Jesus","Lopez", "Masculino", "311 6987561", "Ernesto Lopez", "jhhlopez64@gmail.com", "Chipre")
#(10539876534, "Jesus","Lopez", "Masculino", "311 6987561", "Ernesto Lopez", "jhhlopez64@gmail.com", "Chipre")


# getter && setter STARTS
    # Getter para dni
    def __str__(self):
        return f"dni : {self.dni} || Nombre del Usuario : {self.name} || Apellido: {self.lastName} || Genero: {self.gender} || Telefono : {self.phoneNumber}"
    def getDni(self):
        return self.dni

    # getter && setter para name
    def getName(self):
        return self.name

    def setName(self, __name):
        self.name = __name

    # getter && setter para lastName
    def getLastName(self):
        return self.lastName

    def setLastName(self, __lastName):
        self.lastName = __lastName

    # getter && setter para Gender
    def getGender(self):
        return self.gender

    def setGender(self, __Gender):
        self.gender = __Gender

    # getter && setter para phoneNumber
    def getPhoneNumber(self):
        return self.phoneNumber

    def setPhoneNumber(self, __phoneNumber):
        self.phoneNumber = __phoneNumber


    