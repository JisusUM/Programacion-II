from time import monotonic
from typing import Any
from typing import Any
from xml.dom.minidom import Element
import easygui as eg
#from SupplierCrud import Proveedor


class Item:
    def __init__(self, iditem:int,nombre:str,monto:int,estado:bool,descripcion:str,tipo:type,proveedor:Any):
        self.iditem:int = iditem
        self.nombre:str = nombre
        self.monto:int = monto
        self.estado:bool = estado
        self.descripcion:str = descripcion 
        self.tipo:type = tipo
        self.proveedor = proveedor
    def __str__(self):
        return f"Nombre= {self.nombre},Monto= {self.monto}"
    def getNombre(self):
        return self.nombre
    def getMonto(self):
        return self.monto
    def setNombre(self,nombre):
        self.nombre = nombre
    def setMonto(self,monto):
        self.monto = monto
    def setEstado(self,estado):
        self.estado = estado
    def setDescripcion(self,descripcion):
        self.descripcion = descripcion
    def setTipo(self,tipo):
        self.tipo = tipo
    def setProveedor(self,proveedor):
        self.proveedor = proveedor


lista = []
if __name__ == '__main__':
    while True:
        msg:str = "Colas Circulares--Clase Item"
        titulo:str = "Opciones a realizar"
        opciones = ["Agregar  accesorio","Eliminar acesorio","Verificar si la cola esta vacia","Mostrar accesorios","Aplicar pila"]
        elementos = print("Elementos en cola: ",len(lista))
        menu = eg.indexbox(msg,titulo,opciones,elementos)
        while True:
            if menu == 0:
                msg1 = "Agregar accesorio"
                titulo1 = "Agregar algun dato en la cola circular"
                opciones1 = ["Agregar","Salir"]
                agrega = eg.indexbox(msg1, titulo1, opciones1)
                if agrega == 0:
                    dato = eg.enterbox(msg ="Agregar accesorio", title="Agrega un dato")
                    lista.append(dato)
                else:
                    break

            if menu == 1:
                msg1 = "Eminar dato"
                titulo1 = "Eliminar algun dato"
                opciones1=["Eliminar","Salir"]
                eliminar = eg.indexbox(msg1, titulo1, opciones1)
                if eliminar == 0: 
                    lista.pop(0)
                    #eg.msgbox(msg:str= "Dato eliminado", title:str="Eliminado",ok_button:str= "ok"):
                else:
                    break

            if menu == 2: 
                if len(lista)>0:
                    eg.msgbox(msg="la cola no se encuentra vacia",title="la cola no esta vacia")
                if len(lista) == 0:
                    eg.msgbox(msg="la cola se encuentra vacia",title="la cola esta vacia")
                break
            if menu == 3:
                eg.msgbox(msg=str(lista),title="Estado actual de la cola ")
                break
            if menu == 4:
                    while True:
                        msg:str = "Pila--Clase Item"
                        titulo:str = "Opciones a realizar"
                        opciones = ["Agregar  accesorio","Eliminar acesorio","Verificar si la cola esta vacia","Mostrar accesorios"]
                        elementos = print("Elementos en pila: ",len(lista))
                        menu = eg.indexbox(msg,titulo,opciones,elementos)
                        opciones1 = ["Agregar","Salir"]
                        if menu == 1:
                            msg1 = "Agregar datos"
                            titulo1 = "Agregar algun dato en la pila"
                            opciones1 = ["Agregar","Salir"]
                            agrega = eg.indexbox(msg1, titulo1, opciones1)
                            if agrega == 0:
                                dato = eg.enterbox(msg ="Agrega un dato cualquiera", title="Agrega un dato a la pila ")
                                lista.append(dato)
                            else:
                                break
                        if menu == 2: 
                            if len(lista)>0:
                                eg.msgbox(msg="la cola no se encuentra vacia",title="la cola no esta vacia")
                            if len(lista) == 0:
                                eg.msgbox(msg="la cola se encuentra vacia",title="la cola esta vacia")
                            break
                        if menu == 3:
                            eg.msgbox(msg=str(lista),title="Estado actual de la cola ")
                            break   
                    if menu == 5:
                        break
            if menu == 5:
                break
        if menu == 5:
            break