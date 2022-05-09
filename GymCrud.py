import easygui as eg
# Crear clase Gym
class Gym:
    # Constructor
    def __init__(self, nit:int, name:str, address:str, phone:str):
        # Datos de entrada
        self._nit:int = nit
        self._name:str = name
        self._address:str = address
        self._phone:str = phone
        #self._campus = Campus(976431258, "Iron GYM", "8845632", "Villamaria", True, 13, False, User) # Composicion de Campus
       #self.__listCampus:List = []
       #self.__employee = Employee(2375, 'Oscar Andres', '317 8613343', 250000, Role.ADMINISTRATOR, Ranking.DOS)    # Composicion de Empleado
       #self.__listEmployee:List = []


    # Getter and Setter

    def __str__(self):
        return f"Nit : {self._nit} || Nombre del Gimnasio : {self._name} || Dirección : {self._address} || Telefono : {self._phone}"

    def getName(self):
        return self._name
    def getPhone(self):
        return self._phone
    def getAddress(self):
        return self._address
    def setName(self,_name):
        self._name = _name
    def setPhone(self,_phone):
        self._phone = _phone
    def setAddress(self,_address):
        self._address = _address

cola = []
pila = []
if __name__ == '__main__':
    while True:
        msg:str = "Colas Circulares--Clase Gym"
        titulo:str = "Opciones a realizar"
        opciones = ["Agregar Gimnasio","Eliminar Gimnasio","Verificar si la cola esta vacia","Mostrar Gimnasio","Aplicar pila"]
        elementos = print("Elementos en cola: ",len(cola))
        menu = eg.indexbox(msg,titulo,opciones,elementos)
        while True:
            if menu == 0:
                msg1 = "Agregar Gimnasio"
                titulo1 = "Agregar algun dato en la cola circular"
                opciones1 = ["Agregar","Salir"]
                agrega = eg.indexbox(msg1, titulo1, opciones1)
                if agrega == 0:
                    dato = eg.enterbox(msg ="Agregar Gimnasio", title="Agrega un dato")
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
                        opciones = ["Agregar a la pila","Eliminar elemento","Verificar si la cola esta vacia","Mostrar accesorios","Salir"]
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