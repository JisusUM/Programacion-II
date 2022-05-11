class Campus:
    # Constructor ###
    def __init__(self, __campusNit:int, __campusName: str, __campusPhone: str,
                __campusAddreess: str, __sizeParking: int):
        # Datos de entrada
        self._campusNit = __campusNit
        self._campusName = __campusName
        self._campusPhone = __campusPhone
        self._campusAddreess = __campusAddreess
        self._sizeParking = __sizeParking
        
    # Getter and Setter

    def __str__(self):
        return f"Nit : {self._campusNit} || Nombre : {self._campusName} || Telefono : {self._campusPhone} || Dirección : {self._campusAddreess} || Número de parqueaderos : {self._sizeParking}"

    def getCampusName(self):
        return self.__campusName
    def getCampusPhone(self):
        return self.__campusPhone
    def getCampusAddress(self):
        return self.__campusAddreess
    def setCampusName(self,__campusName):
        self.__campusName = __campusName
    def setCampusPhone(self,__campusPhone):
        self.__campusPhone = __campusPhone
    def setCampusAddreess(self,__campusAddreess):
        self.__campusAddreess = __campusAddreess




cola = []
pila = []
if __name__ == '__main__':
    while True:
        msg:str = "Colas Circulares--Clase Campus"
        titulo:str = "Opciones a realizar"
        opciones = ["Agregar Campus","Eliminar Campus","Verificar si la cola esta vacia","Mostrar Campus","Aplicar pila"]
        elementos = print("Elementos en cola: ",len(cola))
        menu = eg.indexbox(msg,titulo,opciones,elementos)
        while True:
            if menu == 0:
                msg1 = "Agregar Campus"
                titulo1 = "Agregar algun dato en la cola circular"
                opciones1 = ["Agregar","Salir"]
                agrega = eg.indexbox(msg1, titulo1, opciones1)
                if agrega == 0:
                    dato = eg.enterbox(msg ="Agregar Campus", title="Agrega un dato")
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


