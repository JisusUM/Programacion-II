from asyncore import read
from typing import Any, Type
from Enums import Eps, Rh
from datetime import time, datetime
from productCrud import Product
from itemCrud import Item
from SupplierCrud import Proveedor
from GymCrud import Gym
from CampusCrud import Campus
from userCrud import user

if __name__ == '__main__':
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
        opcion = ' '
        while(opcion != 'x'):
            print("--------------------------------")
            print("0 - Buscar Item")
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
            #elif(opcion == '0'):
                #buscarPorID()
            else:
                print("Opcion incorrecta")
    
    def partition(listaProduct, start, end, compare_func):
        pivot = listaProduct[start]
        low = start + 1
        high = end

        while True:
            while low <= high and compare_func(listaProduct[high], pivot):
                high = high - 1

            while low <= high and not compare_func(listaProduct[low], pivot):
                low = low + 1

            if low <= high:
                listaProduct[low], listaProduct[high] = listaProduct[high], listaProduct[low]
            else:
                break

        listaProduct[start], listaProduct[high] = listaProduct[high], listaProduct[start]

        return high

    def quick_sort(listaProduct, start, end, compare_func):
        if start >= end:
            return

        p = partition(listaProduct, start, end, compare_func)
        quick_sort(listaProduct, start, p-1, compare_func)
        quick_sort(listaProduct, p+1, end, compare_func)

    listaProduct = []
    product1 = Product(5,'b',2000,'col',datetime(2023,3,12),True,Any)
    product2 = Product(8,'a',1500,'cool',datetime(2023,3,12),True,Any)
    product3 = Product(1,'a',800,'cool',datetime(2023,3,12),True,Any)
    product4 = Product(2,'a',3000,'cool',datetime(2023,3,12),True,Any)
    product5 = Product(4,'a',2100,'cool',datetime(2023,3,12),True,Any)
    listaProduct.append(product1)
    listaProduct.append(product2)
    listaProduct.append(product3)
    listaProduct.append(product4)
    listaProduct.append(product5)
    
    quick_sort(listaProduct, 0, len(listaProduct) - 1, lambda x, y: x.precio < y.precio)
    for Product in listaProduct:
        print(Product)
    
    #Algoritmo de Buscar 
    """def buscarPorID():
        def busqueda_binaria(listaProduct, busqueda):
            izquierda, derecha = 0, len(listaProduct) - 1
            while izquierda <= derecha:
                indiceDelElementoDelMedio = (izquierda + derecha) // 2
                elementoDelMedio = listaProduct[indiceDelElementoDelMedio]
                if elementoDelMedio == busqueda:
                    return indiceDelElementoDelMedio
                if busqueda < elementoDelMedio:
                    derecha = indiceDelElementoDelMedio - 1
                else:
                    izquierda = indiceDelElementoDelMedio + 1
            # Si salimos del ciclo significa que no existe el valor
            return -1

        
        #Probar con listaProduct de cadenas
        
        listaProduct = []
        print("La otra lista es:", listaProduct)
        busqueda = str(input("\n ingresa  nombre product  de la listaProduct anterior:"))
        indice = busqueda_binaria(listaProduct, busqueda)
        print("El elemento {} está en el índice {}".format(busqueda, indice))"""

    def optItem():
        def agregar(): # funcion o metodo
            iditem = int(input("Ingrese el id del item: "))
            nombre = str(input("ingrese el nombre del item: "))
            monto = int(input("ingrese el monto: "))
            estado = bool(input("Si- True - No - False: "))
            descripcion =str(input("ingrese la descripcion: "))
            tipo = str (input ("ingrese el tipo: "))
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
        opcion = ' '
        while(opcion != 'x'):
            print("--------------------------------")
            print("0 - Buscar Item")
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
            #elif(opcion == '0'):
                #buscarPorID() 
            else:
                print("Opcion incorrecta")
    def partition(listaItem, start, end, compare_func):
        pivot = listaItem[start]
        low = start + 1
        high = end

        while True:
            while low <= high and compare_func(listaItem[high], pivot):
                high = high - 1

            while low <= high and not compare_func(listaItem[low], pivot):
                low = low + 1

            if low <= high:
                listaItem[low], listaItem[high] = listaItem[high], listaItem[low]
            else:
                break

        listaItem[start], listaItem[high] = listaItem[high], listaItem[start]

        return high

    def quick_sort(listaItem, start, end, compare_func):
        if start >= end:
            return

        p = partition(listaItem, start, end, compare_func)
        quick_sort(listaItem, start, p-1, compare_func)
        quick_sort(listaItem, p+1, end, compare_func)

    #Inicio del programa
    listaItem = []
    item1=Item('1','Colchoneta',8,'activo','Ejercicios ABS','Stool','Jisus')
    item2=Item('2','balones',1,'activo','Ejercicios ','Stool','adidas')
    item3=Item('3','Cuerdas',30,'activo','Ejercicios ','Stool','adidas')
    item4=Item('4','Sillas',15,'activo','Ejercicios ','Stool','adidas')
    item5=Item('5','Guantes',45,'activo','Ejercicios ','Stool','adidas')
    listaItem.append(item1.tipo)
    listaItem.append(item2)
    listaItem.append(item3)
    listaItem.append(item4)
    listaItem.append(item5)

    quick_sort(listaItem, 0, len(listaItem) - 1, lambda x, y: x.monto < y.monto)
    for Item in listaItem:
        print(Item)

    #Algoritmo de Buscar 
    """def buscarPorID():
        def busqueda_binaria(listaItem, busqueda):
            izquierda, derecha = 0, len(listaItem) - 1
            while izquierda <= derecha:
                indiceDelElementoDelMedio = (izquierda + derecha) // 2
                elementoDelMedio = listaItem[indiceDelElementoDelMedio]
                if elementoDelMedio == busqueda:
                    return indiceDelElementoDelMedio
                if busqueda < elementoDelMedio:
                    derecha = indiceDelElementoDelMedio - 1
                else:
                    izquierda = indiceDelElementoDelMedio + 1
            # Si salimos del ciclo significa que no existe el valor
            return -1

        
        Probar con listaItem de cadenas
        
        listaItem = []
        print("La otra lista es:", listaItem)
        busqueda = str(input("\n ingresa  nombre Item  de la listaItem anterior:"))
        indice = busqueda_binaria(listaItem, busqueda)
        print("El elemento {} está en el índice {}".format(busqueda, indice))"""


    def optProveedor():
        def agregar(): # funcion o metodo
            nit = int(input("Ingrese el Nit: "))
            nombre = str(input("ingrese el nombre del proveedor: "))
            telefono = str(input("ingrese el numero telefonico: "))
            correo = str(input("Ingrese el correo electronico"))
            itemNuevo = Proveedor(nit,nombre,telefono,correo)
            lista.append(itemNuevo)#append lo que hace es agragar en la cola el nuevo dato , depes del ultimo elemento + 1
            lista = []
            #print(itemNuevo)

        def informar():
            print("")
            print("-----informe-----")
            for indice in range(0, len(lista)):
                print(f"{indice +1} - {lista[indice]}")

        def borrar():
            informar()
            indice =int(input("Ingrese el numero  de item que desea eliminar: "))
            print(f"Esta seguro/a de eliminar a {lista[indice -1].getNombre()} {lista[indice -1].getTelefono()} {lista[indice -1].getCorreo()}")
            respuesta = input("S- Borrar - N - No borrar ")
            if (respuesta == "s"):
                lista.remove(lista[indice -1])

        def modificar():
                informar()
                indice =int(input("Ingrese el numero de item que desea modificar: "))
                nombre = input("ingrese nuevo nombre: ")
                lista[indice -1].setNombre(nombre)
                telefono = input("ingrese nuevo telefono: ")
                lista[indice -1].setTelefono(telefono)
                correo = input("ingrese nuevo correo: ")
                lista[indice -1].setCorreo(correo)
        opcion = ' '
        while(opcion != 'x'):
            print("--------------------------------")
            print("0 - Buscar Item")
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
            #elif(opcion == '0'):
                #buscarPorID()
            else:
                print("Opcion incorrecta")

    def partition(lista, start, end, compare_func):
        pivot = lista[start]
        low = start + 1
        high = end

        while True:
            while low <= high and compare_func(lista[high], pivot):
                high = high - 1

            while low <= high and not compare_func(lista[low], pivot):
                low = low + 1

            if low <= high:
                lista[low], lista[high] = lista[high], lista[low]
            else:
                break

        lista[start], lista[high] = lista[high], lista[start]

        return high

    def quick_sort(lista, start, end, compare_func):
        if start >= end:
            return

        p = partition(lista, start, end, compare_func)
        quick_sort(lista, start, p-1, compare_func)
        quick_sort(lista, p+1, end, compare_func)
        #Inicio del programa
    lista = []
    item1=Proveedor(895053265,"COlCALDAS","3205437504","caldas@gmail.com")
    item2=Proveedor(895052665,"COl","32054315204","cals@gmail.com")
    item3=Proveedor(895053265,"COlCALDAS","3205437504","caldas@gmail.com")
    item4=Proveedor(895052665,"COl","32054315204","cals@gmail.com")
    item5=Proveedor(895053265,"COlCALDAS","3205437504","caldas@gmail.com")
    item6=Proveedor(895052665,"COl","32054315204","cals@gmail.com")
    lista.append(item1)
    lista.append(item2)
    lista.append(item3)
    lista.append(item4)
    lista.append(item5)
    lista.append(item6)
    quick_sort(lista, 0, len(lista) - 1, lambda x, y: x.nit < y.nit)
    for Proveedor in lista:
        print(Proveedor)
    
    #Algoritmo de Buscar 
    """def buscarPorID():
        def busqueda_binaria(lista, busqueda):
            izquierda, derecha = 0, len(lista) - 1
            while izquierda <= derecha:
                indiceDelElementoDelMedio = (izquierda + derecha) // 2
                elementoDelMedio = lista[indiceDelElementoDelMedio]
                if elementoDelMedio == busqueda:
                    return indiceDelElementoDelMedio
                if busqueda < elementoDelMedio:
                    derecha = indiceDelElementoDelMedio - 1
                else:
                    izquierda = indiceDelElementoDelMedio + 1
            # Si salimos del ciclo significa que no existe el valor
            return -1

        
        Probar con lista de cadenas
        
        lista = []
        print("La otra lista es:", lista)
        busqueda = str(input("\n ingresa  nombre product  de la lista anterior:"))
        indice = busqueda_binaria(lista, busqueda)
        print("El elemento {} está en el índice {}".format(busqueda, indice))"""

       
    def optGym():
        def create():
            _nit = int(input("Ingrese el Nit : "))
            _name= str(input("Ingrese el nombre del gimnasio: "))
            _address = str(input("Ingrese la dirección: "))
            _phone = str(input("Ingrese telefono: "))
            nuevoGym = Gym(_nit, _name, _address, _phone)
            list.append(nuevoGym)
            print(nuevoGym)

        def listar():
            print("  ")
            print("-----Informe-----")
            for indice in range(0, len(list)):
                print(f"{indice + 1 } - {list[indice]}")


        def delete():
            listar()
            indice = int(input("Ingrese el numero del Gimnasio a eliminar"))
            print(f"Esta seguro/a de eliminar a {list[indice -1].getName()} {list[indice -1].getPhone()} {list[indice -1].getAddress()}")
            respuesta = input("S- si N- no").lower()
            if (respuesta == "s"):
                list.remove(list[indice - 1])

        def modificar():
            listar()
            indice = int(input("Ingrese el numero del gimnasio a modificar: "))
            _name = input("Ingrese el nuevo nombre del gimnasio: ")
            list[indice - 1].setName(_name)
            _address = input("Ingrese la nueva dirección: ")
            list[indice - 1].setAddress(_address)
            _phone = input("Ingrese el nuevo telefono: ")
            list[indice - 1].setName(_phone)
        opt = ''
        while (opt != "x"):
            opt = str(input("""  Ingrese una de las siguientes opciones
        //-----------//-----------//-----------//
        C-) CREAR NUEVO GIMNASIO
        R-) LISTAR GIMNASIOS
        U-) MODIFICAR GIMNASIO
        D-) ELIMINAR GIMNASIO
        X-) SALIR
        """).lower())
        #F-) BUSCAR GIMNASIO

            if opt == 'x':
                print('Hasta Pronto')
            if opt == 'c':
                create()
            if opt == 'r':
                listar()
            if opt == 'u':
                modificar()
            if opt == 'd':
                delete()
            else:
                print("Opcion incorrecta")

    def partition(list, start, end, compare_func):
        pivot = list[start]
        low = start + 1
        high = end

        while True:
            while low <= high and compare_func(list[high], pivot):
                high = high - 1

            while low <= high and not compare_func(list[low], pivot):
                low = low + 1

            if low <= high:
                list[low], list[high] = list[high], list[low]
            else:
                break

        list[start], list[high] = list[high], list[start]

        return high

    def quick_sort(list, start, end, compare_func):
        if start >= end:
            return

        p = partition(list, start, end, compare_func)
        quick_sort(list, start, p-1, compare_func)
        quick_sort(list, p+1, end, compare_func)
            
        list=[]
        gym1 = Gym(900712196, "European Hardcore", "Chipre", "311 6987561")
        list.append(gym1)
        gym2 = Gym(800206239, "MMA Training", "La Sultana", "315 9876325")
        list.append(gym2)
        quick_sort(list, 0, len(list) - 1, lambda x, y: x.nit < y.nit)
        for Gym in list:
            print(Gym)


    def optCampus():
        def createC():
            _campusNit = str(input("Ingrese el Nit : "))
            _campusName= str(input("Ingrese el nombre del gimnasio: "))
            _campusPhone = str(input("Ingrese la dirección: "))
            _campusAddreess = str(input("Ingrese telefono: "))
            nuevoGym = Campus(_campusNit,_campusName,_campusPhone,_campusAddreess)
            campus.append(nuevoGym)
            print(nuevoGym)

        def listarC():
            print("  ")
            print("-----Informe-----")
            for indice in range(0, len(campus)):
                print(f"{indice + 1 } - {campus[indice]}")


        def deleteC():
            listarC()
            indice = int(input("Ingrese el numero del Gimnasio a eliminar"))
            print(f"Esta seguro/a de eliminar a {campus[indice -1].getCampusName()} {campus[indice -1].getCampusPhone()} {campus[indice -1].getCampusAddreess()}")
            respuesta = input("S- si N- no").lower()
            if (respuesta == "s"):
                campus.remove(campus[indice - 1])

        def modificarC():
            listarC()
            indice = int(input("Ingrese el numero del gimnasio a modificar: "))
            _campusName = input("Ingrese el nuevo nombre del gimnasio: ")
            campus[indice - 1].setCampusName(_campusName)
            _campusPhone = input("Ingrese la nueva dirección: ")
            campus[indice - 1].setCampusPhone(_campusPhone)
            _campusAddreess = input("Ingrese el nuevo telefono: ")
            campus[indice - 1].setCampusAddreess(_campusAddreess)
        opt = ''
        while (opt != "x"):
            opt = str(input("""  Ingrese una de las siguientes opciones
        //-----------//-----------//-----------//
        C-) CREAR NUEVO CAMPUS
        R-) LISTAR CAMPUS
        U-) MODIFICAR CAMPUS
        D-) ELIMINAR CAMPUS
        X-) SALIR
        """).lower())
        #F-) BUSCAR GIMNASIO

            if opt == 'x':
                print('Hasta Pronto')
            if opt == 'c':
                createC()
            if opt == 'r':
                listarC()
            if opt == 'u':
                modificarC()
            if opt == 'd':
                deleteC()
            else:
                print("Opcion incorrecta")
        
    def partition(campus, start, end, compare_func):
        pivot = campus[start]
        low = start + 1
        high = end

        while True:
            while low <= high and compare_func(campus[high], pivot):
                high = high - 1

            while low <= high and not compare_func(campus[low], pivot):
                low = low + 1

            if low <= high:
                campus[low], campus[high] = campus[high], campus[low]
            else:
                break

        campus[start], campus[high] = campus[high], campus[start]

        return high

    def quick_sort(campus, start, end, compare_func):
        if start >= end:
            return

        p = partition(campus, start, end, compare_func)
        quick_sort(campus, start, p-1, compare_func)
        quick_sort(campus, p+1, end, compare_func)

    campus=[]
    """campus1 = Campus("900712196", "European Hardcore", "3205456526", "ldsjfodsjfoisa@gmail.com")
    campus.append(campus1)
    campus2 = Campus("900712196", "European Hardcore", "3205456526", "ldsjfodsjfoisa@gmail.com")
    campus.append(campus2)"""
    quick_sort(campus, 0, len(campus) - 1, lambda x, y: x.campusNit < y.campusNit)
    for Campus in campus:
        print(Campus)
    
    def optUser():
        def createC():
            __dni = str(input("Ingrese el Nit : "))
            __name=str(input("Ingrese el nombre del gimnasio: "))
            __lastName= str(input("Ingrese la dirección: "))
            __gender = str(input(""))
            __phoneNumber = str(input("Ingrese telefono: "))
            nuevoUser = user(__dni,__name,__lastName,__gender,__phoneNumber)
            campus.append(nuevoUser)
            print(nuevoUser)

        def listarC():
            print("  ")
            print("-----Informe-----")
            for indice in range(0, len(campus)):
                print(f"{indice + 1 } - {campus[indice]}")


        def deleteC():
            listarC()
            indice = int(input("Ingrese el numero del Gimnasio a eliminar"))
            print(f"Esta seguro/a de eliminar a {campus[indice -1].getCampusName()} {campus[indice -1].getDni()} {campus[indice -1].getName()}")
            respuesta = input("S- si N- no").lower()
            if (respuesta == "s"):
                campus.remove(campus[indice - 1])

        def modificarC():
            listarC()
            indice = int(input("Ingrese el numero del gimnasio a modificar: "))
            __name= input("Ingrese el nuevo nombre del gimnasio: ")
            campus[indice - 1].setName(__name)
            __lastname = input("Ingrese la nueva dirección: ")
            campus[indice - 1].setLastName(__lastname)
            __gender= input("Ingrese el nuevo telefono: ")
            campus[indice - 1].setGender(__gender)
        opt = ''
        while (opt != "x"):
            opt = str(input("""  Ingrese una de las siguientes opciones
        //-----------//-----------//-----------//
        C-) CREAR NUEVO USUARIO
        R-) LISTAR USUARIO
        U-) MODIFICAR USUARIO
        D-) ELIMINAR USUARIO
        X-) SALIR
        """).lower())
        #F-) BUSCAR GIMNASIO

            if opt == 'x':
                print('Hasta Pronto')
            if opt == 'c':
                createC()
            if opt == 'r':
                listarC()
            if opt == 'u':
                modificarC()
            if opt == 'd':
                deleteC()
            else:
                print("Opcion incorrecta")
        
    def partition(campus, start, end, compare_func):
        pivot = campus[start]
        low = start + 1
        high = end

        while True:
            while low <= high and compare_func(campus[high], pivot):
                high = high - 1

            while low <= high and not compare_func(campus[low], pivot):
                low = low + 1

            if low <= high:
                campus[low], campus[high] = campus[high], campus[low]
            else:
                break

        campus[start], campus[high] = campus[high], campus[start]

        return high

    def quick_sort(campus, start, end, compare_func):
        if start >= end:
            return

        p = partition(campus, start, end, compare_func)
        quick_sort(campus, start, p-1, compare_func)
        quick_sort(campus, p+1, end, compare_func)

    def menu():
        opt:str = ""
        while (opt != "x"):
            opt = str(input("""  Ingrese una de las siguientes opciones
    //-----------//-----------//-----------//
    2-) MODULO ITEMS
    3-) MODULO PROVEEDORES
    4-) MODULO PRODUCTOS
    5-) MODULO GYM
    6-) MODULO CAMPUS
    7-) MODULO USUARIO
    0-) SALIR
    """).lower())
    #F-) BUSCAR USUARIO
            if opt == '0':
                print('Adios')
                break
            elif opt == '4':
                optProducto()
            elif opt == '2':
                optItem()
            elif opt == '3':
                optProveedor()
            elif opt == '5':
                optGym()
            elif opt == '6':
                optCampus()
            elif opt == '7':
                optUser()
            else:
                print("Opcion incorrecta")
    menu()