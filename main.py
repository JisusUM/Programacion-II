    # def read(data):
    #     result = list(map(lambda a,b,c,d,e,f,g,h:(a,b,c,d,e,f,g,h), data[0], data[1], data[2], data[3], data[4], data[5], data[6], data[7]))
    #     print(result)
from asyncore import read
from typing import Any, Type
from Enums import Eps, Rh
from datetime import time, datetime
from itemCrud import Item
from productCrud import Product
from SupplierCrud import Proveedor
#from GymCrud import Gym
#from CampusCrud import Campus

if __name__ == '__main__':
    def optItem():
        def agregar(): # funcion o metodo
            iditem = int(input("Ingrese el id del item: "))
            nombre = str(input("ingrese el nombre del item: "))
            monto = float(input("ingrese el monto: "))
            estado = bool(input("Si- True - No - False: "))
            descripcion =str(input("ingrese la descripcion: "))
            tipo = type (input ("ingrese el tipo: "))
            proveedor = input ("ingrese el proveedor: ")
            itemNuevo = Item(iditem,nombre,monto,estado,descripcion,tipo,proveedor)
            listaItem.append(itemNuevo)#append lo que hace es agragar en la cola el nuevo dato , depes del ultimo elemento + 1
            #print(itemNuevo)

        def informar():
            print("")
            print("-----informe-----")
            for indice in range(0, len(listaItem)):
                print(f"{indice +1} - {listaItem[indice]}")

        def borrar():
            informar()
            indice =int(input("Ingrese el numero  de item que desea eliminar: "))
            print(f"Esta seguro/a de eliminar a {listaItem[indice -1].getNombre()} {listaItem[indice -1].getMonto()}")
            respuesta = input("S- Borrar - N - No borrar ")
            if (respuesta == "s"):
                listaItem.remove(listaItem[indice -1])

        def modificar():
                informar()
                indice =int(input("Ingrese el numero de item que desea modificar: "))
                nombre = input("ingrese nuevo nombre: ")
                listaItem[indice -1].setNombre(nombre)
                monto = input("ingrese nuevo monto: ")
                listaItem[indice -1].setMonto(monto)
                estado = input("ingrese nuevo estado: ")
                listaItem[indice -1].setEstado(estado)
                descripcion = input("ingresie nueva descripción: ")
                listaItem[indice -1].setDescripcion(descripcion)
                tipo = input("ingrese nuevo tipo: ")
                listaItem[indice -1].setTipo(tipo)
                proveedor = input("ingrese nuevo proveedor: ")
                listaItem[indice -1].setProveedor(proveedor)

        #Inicio del programa
        listaItem = []
        item1=Item('1','Colchoneta','2','activo','Ejercicios ABS','Stool','Jisus')
        item2=Item('2','balones','10','activo','Ejercicios ','Stool','adidas')
        listaItem.append(item1)
        listaItem.append(item2)
        opcion = ' '
        while(opcion != 'x'):
            print("--------------------------------")
            print("1 - Agregar Item")
            print("2 - Modificar Item")
            print("3 - Mostrar Item")
            print("4 - Borrar item")
            print("x - Salir")
            opcion = input("ingrese la opcion deseada: ")
            if(opcion == "x"):
                print("Saliendo...")
            elif(opcion == '1'):
                agregar()
            elif(opcion == '3'):
                informar()
            elif(opcion == '4'):
                borrar()
            elif(opcion == '2'):
                modificar() 
            else:
                print("Opcion incorrecta")

    def optProducto():
        def agregar(): # funcion o metodo
            productId =int(input("Ingrese el id del producto: "))
            productNombre = str(input("ingrese el nombre del producto: "))
            precio = float(input("ingrese el precio: "))
            marca = str(input("ingresa la marca: "))
            vencimiento =str(input("ingrese el vencimiento  "))
            disponible = bool(input("Si- True - No - False: "))
            proveedor = str(input("ingrese el proveedor: "))
            productNuevo = Product(productId,productNombre,precio,marca,vencimiento,disponible,proveedor)
            listaProduct.append(productNuevo)#append lo que hace es agragar en la cola el nuevo dato , depes del ultimo elemento + 1
            #print(itemNuevo)

        def informar():
            print("")
            print("-----informe-----")
            for indice in range(0, len(listaProduct)):
                print(f"{indice +1} - {listaProduct[indice]}")

        def borrar():
            informar()
            indice =int(input("Ingrese el numero  de item que desea eliminar: "))
            print(f"Esta seguro/a de eliminar a {listaProduct[indice -1].getProductNombre()} {listaProduct[indice -1].getPrecio()}")
            respuesta = input("S- Borrar - N - No borrar ")
            if (respuesta == "s"):
                listaProduct.remove(listaProduct[indice -1])

        def modificar():
            informar()
            indice =int(input("Ingrese el numero de producto que desea modificar: "))
            productNombre = input("ingrese nuevo nombre producto: ")
            listaProduct[indice -1].setProductNombre(productNombre)
            precio= input("ingrese nuevo precio: ")
            listaProduct[indice -1].setPrecio(precio)
            marca = input("ingrese nuevo marca: ")
            listaProduct[indice -1].setMarca(marca)
            vencimiento = input("ingresie nuevo  fecha de vencimiento:  ")
            listaProduct[indice -1].setVencimiento(vencimiento)
            disponible = input("ingreso la validación: " )
            listaProduct[indice -1].setDisponible(disponible)
            proveedor = input("ingrese nuevo proveedor: ")
            listaProduct[indice -1].setProveedor(proveedor)

        #Inicio del programa
        listaProduct = []
        product1 = Product(1,'cc',0.1,'col', datetime(2023,3,12),True,Any)
        product2= Product(2,'cmc',5.1,'cool', datetime(2023,3,12),True,Any)
        listaProduct.append(product1)
        listaProduct.append(product2)
        opcion = ' '
        while(opcion != 'x'):
            print("--------------------------------")
            print("1 - Agregar Item")
            print("2 - Modificar Item")
            print("3 - Mostrar Item")
            print("4 - Borrar item")
            print("x - Salir")
            opcion = input("ingrese la opcion deseada: ")
            if(opcion == "x"):
                print("Saliendo...")
            elif(opcion == '1'):
                agregar()
            elif(opcion == '3'):
                informar()
            elif(opcion == '4'):
                borrar()
            elif(opcion == '2'):
                modificar() 
            else:
                print("Opcion incorrecta")

    def optProveedor():
        def agregar(): # funcion o metodo
            nit = int(input("Ingrese el Nit: "))
            nombre = str(input("ingrese el nombre del proveedor: "))
            telefono = str(input("ingrese el numero telefonico: "))
            correo = str(input("Ingrese el correo electronico"))
            itemNuevo = Proveedor(nit,nombre,telefono,correo)
            listaItem.append(itemNuevo)#append lo que hace es agragar en la cola el nuevo dato , depes del ultimo elemento + 1
            #print(itemNuevo)

        def informar():
            print("")
            print("-----informe-----")
            for indice in range(0, len(listaItem)):
                print(f"{indice +1} - {listaItem[indice]}")

        def borrar():
            informar()
            indice =int(input("Ingrese el numero  de item que desea eliminar: "))
            print(f"Esta seguro/a de eliminar a {listaItem[indice -1].getNombre()} {listaItem[indice -1].getTelefono()} {listaItem[indice -1].getCorreo()}")
            respuesta = input("S- Borrar - N - No borrar ")
            if (respuesta == "s"):
                listaItem.remove(listaItem[indice -1])

        def modificar():
                informar()
                indice =int(input("Ingrese el numero de item que desea modificar: "))
                nombre = input("ingrese nuevo nombre: ")
                listaItem[indice -1].setNombre(nombre)
                telefono = input("ingrese nuevo telefono: ")
                listaItem[indice -1].setTelefono(telefono)
                correo = input("ingrese nuevo correo: ")
                listaItem[indice -1].setCorreo(correo)

        #Inicio del programa
        listaItem = []
        item1=Proveedor(895053265,"COlCALDAS","3205437504","caldas@gmail.com")
        item2=Proveedor(895052665,"COl","32054315204","cals@gmail.com")
        item3=Proveedor(895053265,"COlCALDAS","3205437504","caldas@gmail.com")
        item4=Proveedor(895052665,"COl","32054315204","cals@gmail.com")
        item5=Proveedor(895053265,"COlCALDAS","3205437504","caldas@gmail.com")
        item6=Proveedor(895052665,"COl","32054315204","cals@gmail.com")
        listaItem.append(item1)
        listaItem.append(item2)
        listaItem.append(item3)
        listaItem.append(item4)
        listaItem.append(item5)
        listaItem.append(item6)

        opcion = ' '
        while(opcion != 'x'):
            print("--------------------------------")
            print("1 - Agregar Item")
            print("2 - Modificar Item")
            print("3 - Mostrar Item")
            print("4 - Borrar item")
            print("x - Salir")
            opcion = input("ingrese la opcion deseada: ")
            if(opcion == "x"):
                print("Saliendo...")
            elif(opcion == '1'):
                agregar()
            elif(opcion == '3'):
                informar()
            elif(opcion == '4'):
                borrar()
            elif(opcion == '2'):
                modificar() 
            else:
                print("Opcion incorrecta")

    def menu():
        opt:str = ""
        while (opt != "x"):
            opt = str(input("""  Ingrese una de las siguientes opciones
    //-----------//-----------//-----------//
    1-) MODULO USUARIO
    2-) MODULO ITEMS
    3-) MODULO PROVEEDORES
    4-) MODULO PRODUCTOS
    5-) MODULO GYM
    6-) MODULO CAMPUS
    0-) SALIR
    """).lower())
    #F-) BUSCAR USUARIO
            if opt == '0':
                print('Adios')
                break
            elif opt == '1':
                optUser()
            elif opt == '2':
                optItem()
            elif opt == '3':
                optProveedor()
            elif opt == '4':
                optProducto()
            elif opt == '5':
                optGym()
            elif opt == '6':
                optCampus()
            else:
                print("Opcion incorrecta")
    menu()