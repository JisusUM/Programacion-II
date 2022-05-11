class user:
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




cola = []
pila = []
if __name__ == '__main__':
    while True:
        msg:str = "Colas Circulares--Clase Item"
        titulo:str = "Opciones a realizar"
        opciones = ["Agregar Usuario","Eliminar acesorio","Verificar si la cola esta vacia","Mostrar Usuarios","Aplicar pila"]
        elementos = print("Elementos en cola: ",len(cola))
        menu = eg.indexbox(msg,titulo,opciones,elementos)
        while True:
            if menu == 0:
                msg1 = "Agregar Usuario"
                titulo1 = "Agregar algun dato en la cola circular"
                opciones1 = ["Agregar","Salir"]
                agrega = eg.indexbox(msg1, titulo1, opciones1)
                if agrega == 0:
                    dato = eg.enterbox(msg ="Agregar Usuario", title="Agrega un dato")
                    cola.append(dato)
                else:
                    break

            if menu == 1:
                msg1 = "Eminar dato"
                titulo1 = "Eliminar algun dato"
                opciones1=["Eliminar","Salir"]
                eliminar = eg.indexbox(msg1, titulo1, opciones1)
                if eliminar == 0: 
                    cola.pop(0)
                    #eg.msgbox(msg:str= "Dato eliminado", title:str="Eliminado",ok_button:str= "ok"):
                else:
                    break

            if menu == 2: 
                if len(cola)>0:
                    eg.msgbox(msg="la cola no se encuentra vacia",title="la cola no esta vacia")
                if len(cola) == 0:
                    eg.msgbox(msg="la cola se encuentra vacia",title="la cola esta vacia")
                break
            if menu == 3:
                eg.msgbox(msg=str(cola),title="Estado actual de la cola ")
                break
            if menu == 4:
                    while True:
                        msg:str = "Pila--Clase Item"
                        titulo:str = "Opciones a realizar"
                        opciones = ["Agregar a la pila","Eliminar elemento","Verificar si la cola esta vacia","Mostrar Usuarios","Salir"]
                        elementos = print("Elementos en pila: ",len(pila))
                        menu = eg.indexbox(msg,titulo,opciones,elementos)
                        if menu == 0:
                            msg1 = "Agregar datos"
                            titulo1 = "Agregar algun dato en la pila"
                            opciones1 = ["Agregar","Salir"]
                            agrega = eg.indexbox(msg1, titulo1, opciones1)
                            if agrega == 0:
                                dato1 = eg.enterbox(msg ="Agrega un dato cualquiera", title="Agrega un dato a la pila ")
                                pila.append(dato1)
                            else:
                                break
                        if menu == 1:
                            msg1 = "Eminar dato"
                            titulo1 = "Eliminar algun dato"
                            opciones1=["Eliminar","Salir"]
                            eliminar = eg.indexbox(msg1, titulo1, opciones1)
                            if eliminar == 0: 
                                n=pila.pop()
                                #eg.msgbox(msg:str= "Dato eliminado", title:str="Eliminado",ok_button:str= "ok"):
                            else:
                                break
                        if menu == 2: 
                            if len(pila)>0:
                                eg.msgbox(msg="la cola no se encuentra vacia",title="la cola no esta vacia")
                            if len(pila) == 0:
                                eg.msgbox(msg="la cola se encuentra vacia",title="la cola esta vacia")
                            break
                        if menu == 3:
                            eg.msgbox(msg=str(pila),title="Estado actual de la cola ")
                            break   
                    if menu == 5:
                        break
            if menu == 5:
                break
        if menu == 5:
            break
    
