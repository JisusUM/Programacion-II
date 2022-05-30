from typing import Any
from datetime import time, datetime
from item import Item
from product import Product
from Supplier import Proveedor
from Gym import Gym
from Campus import Campus
from user import user

if __name__ == '__main__':
    def optItem():
        class Nodo(Item):
            def __init__(self, dato=None, siguiente=None, anterior=None):
                self.dato = dato
                self.siguiente = siguiente
                self.anterior = anterior

        class ListaDoblementeEnlazada(Item):
            def __init__(self):
                self.cabeza = None
                self.cola = None
                self.contador = 0
            
            def insertar(self, dato):
                nodo = Nodo(dato)

                if self.cabeza is None:
                    self.cabeza = nodo
                    self.cola = self.cabeza
                else:
                    nodo.anterior = self.cola
                    self.cola.siguiente = nodo
                    self.cola = nodo
                
                self.contador += 1
            
            def iterar(self):#Metodo de instancia
                actual = self.cabeza

                while actual:
                    dato = actual.dato
                    actual = actual.siguiente
                    yield dato


            def insertar_inicio(self, dato):
                if self.cabeza is not None:
                    nodo = Nodo(dato)
                    nodo.siguiente = self.cabeza
                    self.cabeza.anterior = nodo
                    self.cabeza = nodo

                    self.contador += 1
            
            def eliminar(self, dato):
                actual = self.cabeza
                eliminado = False

                if actual is None:
                    eliminado = False
                elif actual.dato == dato:
                    self.cabeza = actual.siguiente
                    self.cabeza.anterior = None
                    eliminado = True
                elif self.cola.dato == dato:
                    self.cola = self.cola.anterior
                    self.cola.siguiente = None
                    eliminado = True
                else:
                    while actual:
                        if actual.dato == dato:
                            actual.anterior.siguiente = actual.siguiente
                            actual.siguiente.anterior = actual.anterior
                            eliminado = True
                        actual = actual.siguiente
                
                if eliminado:
                    self.contador -= 1
            
            def __getitem__(self, indice):
                if indice >= 1 and indice < self.contador:
                    actual = self.cabeza

                    for _ in range(indice - 1):
                        actual = actual.siguiente
                    
                    return actual.dato
                else:
                    raise Exception('Índice no válido. Está por fuera del rango.')
            
            def __setitem__(self, indice, dato):
                if indice >= 1 and indice < self.contador:
                    actual = self.cabeza

                    for _ in range(indice -1):
                        actual = actual.siguiente
                    
                    actual.dato = dato
                else:
                    raise Exception('Índice no válido. Está por fuera del rango.')
        listaItem = ListaDoblementeEnlazada()
        print('Cantidad antes de insertar un elemento en la lista:', listaItem.contador)

        item1=Item('1','Colchoneta',8,'activo','Ejercicios ABS','Stool','Jisus')
        item2=Item('2','balones',1,'activo','Ejercicios ','Stool','adidas')
        item3=Item('3','Cuerdas',30,'activo','Ejercicios ','Stool','adidas')
        item4=Item('4','Sillas',15,'activo','Ejercicios ','Stool','adidas')
        item5=Item('5','Guantes',45,'activo','Ejercicios ','Stool','adidas')
        print()
        listaItem.insertar(item1)
        listaItem.insertar(item2)
        listaItem.insertar(item3)
        listaItem.insertar(item4)

        print('Cantidad actual de elementos:', listaItem.contador)
        print()

        for d in listaItem.iterar():
            print(d)

        print()

        listaItem.insertar_inicio(item5)
        print('Cantidad de elementos después de insertar el elementos: ', listaItem.contador)

        for d in listaItem.iterar():
            print(d)

        print()

        print('Eliminación de datos:')
        item1 = item1
        listaItem.eliminar(item1)
        print('Cantidad de elementos después de eleminar el elemento: ', listaItem.contador)
        for d in listaItem.iterar():
            print(d)

        print()

        print('Eliminación de datos especificando cualquier elemento:')
        item5 = item5
        print('Cantidad de elementos antes de la eliminación:', listaItem.contador)
        listaItem.eliminar(item5)

        print('Cantidad de elementos después de eleminar el elemento: ', listaItem.contador)
        for d in listaItem.iterar():
            print(d)

        print()

        print('Insertando valores de la lista a partir de un índice:')
        print('Cantidad actual de elementos: %i' % listaItem.contador)
        print('Contenido en la posición 3 antes de la modificación: ' ,listaItem[2])
        item3.nombre = 'Guantes'
        item3.monto = 35
        listaItem[2] = item3.nombre,item3.monto
        print('Contenido en la posición 3 después de la modificación: ', listaItem[2])

    def optProduct():
        class Nodo(Product):
            def __init__(self, dato=None, siguiente=None, anterior=None):
                self.dato = dato
                self.siguiente = siguiente
                self.anterior = anterior

        class ListaDoblementeEnlazada(Product):
            def __init__(self):
                self.cabeza = None
                self.cola = None
                self.contador = 0
            
            def insertar(self, dato):
                nodo = Nodo(dato)

                if self.cabeza is None:
                    self.cabeza = nodo
                    self.cola = self.cabeza
                else:
                    nodo.anterior = self.cola
                    self.cola.siguiente = nodo
                    self.cola = nodo
                
                self.contador += 1
            
            def is_empty(self):  # ¿Está vacía la lista vinculada?
                return self._head == None
            
            def append(self,dato):   #Añadir nodos a la cola
                nodo = Nodo(dato)
                if self.is_empty():
                    self._head=nodo
                else:
                    p = self._head
                    while(p.next!=None):
                        p=p.next
                    p.next=nodo
                    nodo.prior=p
            def insert(self,pos,dato): #Añadir nodo a cualquier posición
                if pos<=0:
                    self.insertar(dato)
                elif pos>(self.length()-1):
                    self.append(dato)
                else:
                    p = self._head
                    nodo = Nodo(dato)
                    count = 0
                    while (count < pos):
                        p = p.next
                        count += 1
                        # Cuando el bucle termina, p apunta a la posición de pos
                        nodo.next = p
                        nodo.prior=p.prior
                        p.prior.next=nodo
                        p.prior=nodo
            
            def iterar(self):#Metodo de instancia
                actual = self.cabeza

                while actual:
                    dato = actual.dato
                    actual = actual.siguiente
                    yield dato


            def insertar_inicio(self, dato):
                if self.cabeza is not None:
                    nodo = Nodo(dato)
                    nodo.siguiente = self.cabeza
                    self.cabeza.anterior = nodo
                    self.cabeza = nodo

                    self.contador += 1
            
            def eliminar(self, dato):
                actual = self.cabeza
                eliminado = False

                if actual is None:
                    eliminado = False
                elif actual.dato == dato:
                    self.cabeza = actual.siguiente
                    self.cabeza.anterior = None
                    eliminado = True
                elif self.cola.dato == dato:
                    self.cola = self.cola.anterior
                    self.cola.siguiente = None
                    eliminado = True
                else:
                    while actual:
                        if actual.dato == dato:
                            actual.anterior.siguiente = actual.siguiente
                            actual.siguiente.anterior = actual.anterior
                            eliminado = True
                        actual = actual.siguiente
                
                if eliminado:
                    self.contador -= 1
            
            def __getitem__(self, indice):
                if indice >= 1 and indice < self.contador:
                    actual = self.cabeza

                    for _ in range(indice - 1):
                        actual = actual.siguiente
                    
                    return actual.dato
                else:
                    raise Exception('Índice no válido. Está por fuera del rango.')
            
            def __setitem__(self, indice, dato):
                if indice >= 1 and indice < self.contador:
                    actual = self.cabeza

                    for _ in range(indice -1):
                        actual = actual.siguiente
                    
                    actual.dato = dato
                else:
                    raise Exception('Índice no válido. Está por fuera del rango.')
        listaProduct = ListaDoblementeEnlazada()
        print('Cantidad antes de insertar un elemento en la lista:', listaProduct.contador)

        product1 = Product(5,'b',2000,'col',datetime(2023,3,12),True,Any)
        product2 = Product(8,'a',1500,'cool',datetime(2023,3,12),True,Any)
        product3 = Product(1,'a',800,'cool',datetime(2023,3,12),True,Any)
        product4 = Product(2,'a',3000,'cool',datetime(2023,3,12),True,Any)
        product5 = Product(4,'a',2100,'cool',datetime(2023,3,12),True,Any)
        listaProduct.insertar(product1)
        listaProduct.insertar(product2)
        listaProduct.insertar(product3)
        listaProduct.insertar(product4)

        print('Cantidad actual de elementos:', listaProduct.contador)
        print()

        for d in listaProduct.iterar():
            print(d)

        print()

        listaProduct.insertar_inicio(product5)
        print('Cantidad de elementos después de insertar el elementos: ', listaProduct.contador)

        for d in listaProduct.iterar():
            print(d)

        print()

        print('Eliminación de datos:')
        product1 = product1
        listaProduct.eliminar(product1)
        print('Cantidad de elementos después de eleminar el elemento: ', listaProduct.contador)
        for d in listaProduct.iterar():
            print(d)

        print()

        print('Eliminación de datos especificando cualquier elemento:')
        product5 = product5
        print('Cantidad de elementos antes de la eliminación:', listaProduct.contador)
        listaProduct.eliminar(product5)

        print('Cantidad de elementos después de eleminar el elemento: ', listaProduct.contador)
        for d in listaProduct.iterar():
            print(d)

        print()

        print('Insertando valores de la lista a partir de un índice:')
        print('Cantidad actual de elementos: %i' % listaProduct.contador)
        print('Contenido en la posición 3 antes de la modificación: ' ,listaProduct[2])
        product5.productId = 20
        product5.productNombre = 'Mancuernas'
        product5.precio = 1000
        listaProduct[2] = product5.productId,product5.productNombre,product5.precio
        print('Contenido en la posición 3 después de la modificación: ', listaProduct[2])

        print('Insertando elemento en cualquier posición ')
        listaProduct = ListaDoblementeEnlazada ()
        #print(listaProduct.is_empty())
        listaProduct.insertar(2)

    def optProveedor():
        class Nodo(Proveedor):
            def __init__(self, dato=None, siguiente=None, anterior=None):
                self.dato = dato
                self.siguiente = siguiente
                self.anterior = anterior

        class ListaDoblementeEnlazada(Proveedor):
            def __init__(self):
                self.cabeza = None
                self.cola = None
                self.contador = 0
            
            def insertar(self, dato):
                nodo = Nodo(dato)

                if self.cabeza is None:
                    self.cabeza = nodo
                    self.cola = self.cabeza
                else:
                    nodo.anterior = self.cola
                    self.cola.siguiente = nodo
                    self.cola = nodo
                
                self.contador += 1
            
            def iterar(self):#Metodo de instancia
                actual = self.cabeza

                while actual:
                    dato = actual.dato
                    actual = actual.siguiente
                    yield dato


            def insertar_inicio(self, dato):
                if self.cabeza is not None:
                    nodo = Nodo(dato)
                    nodo.siguiente = self.cabeza
                    self.cabeza.anterior = nodo
                    self.cabeza = nodo

                    self.contador += 1
            
            def eliminar(self, dato):
                actual = self.cabeza
                eliminado = False

                if actual is None:
                    eliminado = False
                elif actual.dato == dato:
                    self.cabeza = actual.siguiente
                    self.cabeza.anterior = None
                    eliminado = True
                elif self.cola.dato == dato:
                    self.cola = self.cola.anterior
                    self.cola.siguiente = None
                    eliminado = True
                else:
                    while actual:
                        if actual.dato == dato:
                            actual.anterior.siguiente = actual.siguiente
                            actual.siguiente.anterior = actual.anterior
                            eliminado = True
                        actual = actual.siguiente
                
                if eliminado:
                    self.contador -= 1
            
            def __getitem__(self, indice):
                if indice >= 1 and indice < self.contador:
                    actual = self.cabeza

                    for _ in range(indice - 1):
                        actual = actual.siguiente
                    
                    return actual.dato
                else:
                    raise Exception('Índice no válido. Está por fuera del rango.')
            
            def __setitem__(self, indice, dato):
                if indice >= 1 and indice < self.contador:
                    actual = self.cabeza

                    for _ in range(indice -1):
                        actual = actual.siguiente
                    
                    actual.dato = dato
                else:
                    raise Exception('Índice no válido. Está por fuera del rango.')

        lista = ListaDoblementeEnlazada() 
        print('Cantidad antes de insertar un elemento en la lista:', lista.contador)

        item1=Proveedor(895053265,"COlCALDAS","3205437504","caldas@gmail.com")
        item2=Proveedor(895052665,"COl","32054315204","cals@gmail.com")
        item3=Proveedor(895053265,"COlCALDAS","3205437504","caldas@gmail.com")
        item4=Proveedor(895052665,"COl","32054315204","cals@gmail.com")
        item5=Proveedor(895053265,"COlCALDAS","3205437504","caldas@gmail.com")
        item6=Proveedor(895052665,"COl","32054315204","cals@gmail.com")
        print()
        lista.insertar(item1)
        lista.insertar(item2)
        lista.insertar(item3)
        lista.insertar(item4)
        lista.insertar(item5)

        print('Cantidad actual de elementos:', lista.contador)
        print()

        for d in lista.iterar():
            print(d)

        print()

        lista.insertar_inicio(item6)
        print('Cantidad de elementos después de insertar el elementos: ', lista.contador)

        for d in lista.iterar():
            print(d)

        print()

        print('Eliminación de datos:')
        item1 = item1
        lista.eliminar(item1)
        print('Cantidad de elementos después de eleminar el elemento: ', lista.contador)
        for d in lista.iterar():
            print(d)

        print()

        print('Eliminación de datos especificando cualquier elemento:')
        item5 = item5
        print('Cantidad de elementos antes de la eliminación:', lista.contador)
        lista.eliminar(item5)

        print('Cantidad de elementos después de eleminar el elemento: ', lista.contador)
        for d in lista.iterar():
            print(d)

        print()

        print('Insertando valores de la lista a partir de un índice:')
        print('Cantidad actual de elementos: %i' % lista.contador)
        print('Contenido en la posición 2 antes de la modificación: ' ,lista[2])
        item5.nombre = 'COLCLI'
        item5.telefono= '3009121255'
        item5.correo = 'JESUH.@GMAIL.COM'
        lista[2] = item5.nombre,item5.telefono,item5.correo
        print('Contenido en la posición 2 después de la modificación: ', lista[2])

            
    
    def menu():
        opt:str = ""
        while (opt != "x"):
            opt = str(input("""  Ingrese una de las siguientes opciones
    //-----------//-----------//-----------//
    1-) Doublylinkedlist ITEMS
    2-) Doublylinkedlist PRODUCTOS
    3-) Doublylinkedlist PROVEEDORES
    4-) Doublylinkedlist GYM
    5-) Doublylinkedlist CAMPUS
    6-) Doublylinkedlist USUARIO
    0-) SALIR
    """).lower())
            if opt == '0':
                print('Adios')
                break
            elif opt == '1':
                optItem()
            elif opt == '2':
                optProduct()
            elif opt == '3':
                optProveedor()
            elif opt == '4':
                optGym()
            elif opt == '5':
                optCampus()
            elif opt == '6':
                optUser()
            else:
                print("Opcion incorrecta")
    menu()
        



