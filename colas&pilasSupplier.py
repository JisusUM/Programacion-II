import easygui as eg

cola = []
pila = []
if __name__ == '__main__':
    while True:
        msg:str = "Colas Circulares--Clase Item"
        titulo:str = "Opciones a realizar"
        opciones = ["Agregar  accesorio","Eliminar acesorio","Verificar si la cola esta vacia","Mostrar accesorios","Aplicar pila"]
        elementos = print("Elementos en cola: ",len(cola))
        menu = eg.indexbox(msg,titulo,opciones,elementos)
        while True:
            if menu == 0:
                msg1 = "Agregar accesorio"
                titulo1 = "Agregar algun dato en la cola circular"
                opciones1 = ["Agregar","Salir"]
                agrega = eg.indexbox(msg1, titulo1, opciones1)
                if agrega == 0:
                    dato = eg.enterbox(msg ="Agregar accesorio", title="Agrega un dato")
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