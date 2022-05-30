from typing import Any
from datetime import datetime
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

        print('Insertando elemento en cualquier posición ')
        listaProduct = ListaDoblementeEnlazada ()
        #print(listaProduct.is_empty())
        listaProduct.insertar(2)

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
    def optGym():
        class Nodo(Gym):
            def __init__(self, dato=None, siguiente=None, anterior=None):
                self.dato = dato
                self.siguiente = siguiente
                self.anterior = anterior

        class ListaDoblementeEnlazada(Gym):
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
        list=ListaDoblementeEnlazada()
        gym1 = Gym(900712196, "European Hardcore", "Chipre", "311 6987561")
        gym2 = Gym(800206239, "MMA Training", "La Sultana", "315 9876325")
        gym3 = Gym(80950285,"um","centro","323235556")
        gym4 = Gym(8095025,"u","cen","32335556")
        print()
        list.insertar(gym1)
        list.insertar(gym2)
        list.insertar(gym3)

        print('Cantidad actual de elementos:', list.contador)
        print()

        for d in list.iterar():
            print(d)

        print()

        list.insertar_inicio(gym4)
        print('Cantidad de elementos después de insertar el elementos: ', list.contador)

        for d in list.iterar():
            print(d)

        print()

        print('Eliminación de datos:')
        gym1 = gym1
        list.eliminar(gym1)
        print('Cantidad de elementos después de eleminar el elemento: ', list.contador)
        for d in list.iterar():
            print(d)

        print()

        print('Eliminación de datos especificando cualquier elemento:')
        gym2 = gym2
        print('Cantidad de elementos antes de la eliminación:', list.contador)
        list.eliminar(gym2)

        print('Cantidad de elementos después de eleminar el elemento: ', list.contador)
        for d in list.iterar():
            print(d)

        print()

        print('Insertando valores de la lista a partir de un índice:')
        print('Cantidad actual de elementos: %i' % list.contador)
        print('Contenido en la posición 2 antes de la modificación: ' ,list[1])
        gym1._nit = '80580564'
        gym1._name= "uam"
        list[1] = gym1._nit,gym1._name
        print('Contenido en la posición 2 después de la modificación: ', list[1])

    def optCampus():
        class Nodo(Campus):
            def __init__(self, dato=None, siguiente=None, anterior=None):
                self.dato = dato
                self.siguiente = siguiente
                self.anterior = anterior

        class ListaDoblementeEnlazada(Campus):
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
        campus=ListaDoblementeEnlazada()
        campus1 = Campus("900712196", "European Hardcore", "3205456526", "ldsjfodsjfoisa@gmail.com")
        campus2 = Campus("900712196", "European Hardcore", "3205456526", "ldsjfodsjfoisa@gmail.com")
        campus3 = Campus("900712196", "European Hardcore", "3205456526", "ldsjfodsjfoisa@gmail.com")
        campus4 = Campus("900712196", "European Hardcore", "3205456526", "ldsjfodsjfoisa@gmail.com")
        print()
        campus.insertar(campus1)
        campus.insertar(campus2)
        campus.insertar(campus3)
        print('Cantidad actual de elementos:', campus.contador)
        print()

        for d in campus.iterar():
            print(d)

        print()

        campus.insertar_inicio(campus4)
        print('Cantidad de elementos después de insertar el elementos: ', campus.contador)

        for d in campus.iterar():
            print(d)

        print()

        print('Eliminación de datos:')
        campus1 = campus1
        campus.eliminar(campus1)
        print('Cantidad de elementos después de eleminar el elemento: ', campus.contador)
        for d in campus.iterar():
            print(d)

        print()

        print('Eliminación de datos especificando cualquier elemento:')
        campus2 = campus2
        print('Cantidad de elementos antes de la eliminación:', campus.contador)
        campus.eliminar(campus2)

        print('Cantidad de elementos después de eleminar el elemento: ', campus.contador)
        for d in campus.iterar():
            print(d)

        print()

        print('Insertando valores de la lista a partir de un índice:')
        print('Cantidad actual de elementos: %i' % campus.contador)
        print('Contenido en la posición 2 antes de la modificación: ' ,campus[1])
        campus1._nit = '80580564'
        campus1._name= "uam"
        campus[1] = campus1._nit,campus1._name
        print('Contenido en la posición 2 después de la modificación: ', campus[1])

    def optUser():
        class Nodo(user):
            def __init__(self, dato=None, siguiente=None, anterior=None):
                self.dato = dato
                self.siguiente = siguiente
                self.anterior = anterior

        class ListaDoblementeEnlazada(user):
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
        listUser = ListaDoblementeEnlazada()
        user1= user(8555165,'jisus','lopez','masculino','320543154638','false','jhh@gmail.com','calle 50')
        user2= user(8555165,'jisus','lopez','masculino','320543154638','false','jhh@gmail.com','calle 50')
        user3= user(8555165,'jisus','lopez','masculino','320543154638','false','jhh@gmail.com','calle 50')
        user4= user(8555165,'jisus','lopez','masculino','320543154638','false','jhh@gmail.com','calle 50')
        print()
        listUser.insertar(user1)
        listUser.insertar(user2)
        listUser.insertar(user3)

        print('Cantidad actual de elementos:', listUser.contador)
        print()

        for d in listUser.iterar():
            print(d)

        print()

        listUser.insertar_inicio(user4)
        print('Cantidad de elementos después de insertar el elementos: ', listUser.contador)

        for d in listUser.iterar():
            print(d)

        print()

        print('Eliminación de datos:')
        user1 = user1
        listUser.eliminar(user1)
        print('Cantidad de elementos después de eleminar el elemento: ', listUser.contador)
        for d in listUser.iterar():
            print(d)

        print()

        print('Eliminación de datos especificando cualquier elemento:')
        user2 = user2
        print('Cantidad de elementos antes de la eliminación:', listUser.contador)
        listUser.eliminar(user2)

        print('Cantidad de elementos después de eleminar el elemento: ', listUser.contador)
        for d in listUser.iterar():
            print(d)

        print()

        print('Insertando valores de la listUsera a partir de un índice:')
        print('Cantidad actual de elementos: %i' % listUser.contador)
        print('Contenido en la posición 2 antes de la modificación: ' ,listUser[1])
        user1.dni = '80580564'
        user1.name= "uam"
        listUser[1] = user1.dni,user1.name
        print('Contenido en la posición 2 después de la modificación: ', listUser[1])

    def optGym():
        class Nodo(Gym):
            def __init__(self, dato=None, siguiente=None, anterior=None):
                self.dato = dato
                self.siguiente = siguiente
                self.anterior = anterior

        class ListaDoblementeEnlazada(Gym):
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
        list=ListaDoblementeEnlazada()
        gym1 = Gym(900712196, "European Hardcore", "Chipre", "311 6987561")
        gym2 = Gym(800206239, "MMA Training", "La Sultana", "315 9876325")
        gym3 = Gym(80950285,"um","centro","323235556")
        gym4 = Gym(8095025,"u","cen","32335556")
        print()
        list.insertar(gym1)
        list.insertar(gym2)
        list.insertar(gym3)

        print('Cantidad actual de elementos:', list.contador)
        print()

        for d in list.iterar():
            print(d)

        print()

        list.insertar_inicio(gym4)
        print('Cantidad de elementos después de insertar el elementos: ', list.contador)

        for d in list.iterar():
            print(d)

        print()

        print('Eliminación de datos:')
        gym1 = gym1
        list.eliminar(gym1)
        print('Cantidad de elementos después de eleminar el elemento: ', list.contador)
        for d in list.iterar():
            print(d)

        print()

        print('Eliminación de datos especificando cualquier elemento:')
        gym2 = gym2
        print('Cantidad de elementos antes de la eliminación:', list.contador)
        list.eliminar(gym2)

        print('Cantidad de elementos después de eleminar el elemento: ', list.contador)
        for d in list.iterar():
            print(d)

        print()

        print('Insertando valores de la lista a partir de un índice:')
        print('Cantidad actual de elementos: %i' % list.contador)
        print('Contenido en la posición 2 antes de la modificación: ' ,list[1])
        gym1._nit = '80580564'
        gym1._name= "uam"
        list[1] = gym1._nit,gym1._name
        print('Contenido en la posición 2 después de la modificación: ', list[1])

    def optCampus():
        class Nodo(Campus):
            def __init__(self, dato=None, siguiente=None, anterior=None):
                self.dato = dato
                self.siguiente = siguiente
                self.anterior = anterior

        class ListaDoblementeEnlazada(Campus):
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
        campus=ListaDoblementeEnlazada()
        campus1 = Campus("900712196", "European Hardcore", "3205456526", "ldsjfodsjfoisa@gmail.com")
        campus2 = Campus("900712196", "European Hardcore", "3205456526", "ldsjfodsjfoisa@gmail.com")
        campus3 = Campus("900712196", "European Hardcore", "3205456526", "ldsjfodsjfoisa@gmail.com")
        campus4 = Campus("900712196", "European Hardcore", "3205456526", "ldsjfodsjfoisa@gmail.com")
        print()
        campus.insertar(campus1)
        campus.insertar(campus2)
        campus.insertar(campus3)
        print('Cantidad actual de elementos:', campus.contador)
        print()

        for d in campus.iterar():
            print(d)

        print()

        campus.insertar_inicio(campus4)
        print('Cantidad de elementos después de insertar el elementos: ', campus.contador)

        for d in campus.iterar():
            print(d)

        print()

        print('Eliminación de datos:')
        campus1 = campus1
        campus.eliminar(campus1)
        print('Cantidad de elementos después de eleminar el elemento: ', campus.contador)
        for d in campus.iterar():
            print(d)

        print()

        print('Eliminación de datos especificando cualquier elemento:')
        campus2 = campus2
        print('Cantidad de elementos antes de la eliminación:', campus.contador)
        campus.eliminar(campus2)

        print('Cantidad de elementos después de eleminar el elemento: ', campus.contador)
        for d in campus.iterar():
            print(d)

        print()

        print('Insertando valores de la lista a partir de un índice:')
        print('Cantidad actual de elementos: %i' % campus.contador)
        print('Contenido en la posición 2 antes de la modificación: ' ,campus[1])
        campus1._nit = '80580564'
        campus1._name= "uam"
        campus[1] = campus1._nit,campus1._name
        print('Contenido en la posición 2 después de la modificación: ', campus[1])

    def optUser():
        class Nodo(user):
            def __init__(self, dato=None, siguiente=None, anterior=None):
                self.dato = dato
                self.siguiente = siguiente
                self.anterior = anterior

        class ListaDoblementeEnlazada(user):
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
        listUser = ListaDoblementeEnlazada()
        user1= user(8555165,'jisus','lopez','masculino','320543154638','false','jhh@gmail.com','calle 50')
        user2= user(8555165,'jisus','lopez','masculino','320543154638','false','jhh@gmail.com','calle 50')
        user3= user(8555165,'jisus','lopez','masculino','320543154638','false','jhh@gmail.com','calle 50')
        user4= user(8555165,'jisus','lopez','masculino','320543154638','false','jhh@gmail.com','calle 50')
        print()
        listUser.insertar(user1)
        listUser.insertar(user2)
        listUser.insertar(user3)

        print('Cantidad actual de elementos:', listUser.contador)
        print()

        for d in listUser.iterar():
            print(d)

        print()

        listUser.insertar_inicio(user4)
        print('Cantidad de elementos después de insertar el elementos: ', listUser.contador)

        for d in listUser.iterar():
            print(d)

        print()

        print('Eliminación de datos:')
        user1 = user1
        listUser.eliminar(user1)
        print('Cantidad de elementos después de eleminar el elemento: ', listUser.contador)
        for d in listUser.iterar():
            print(d)

        print()

        print('Eliminación de datos especificando cualquier elemento:')
        user2 = user2
        print('Cantidad de elementos antes de la eliminación:', listUser.contador)
        listUser.eliminar(user2)

        print('Cantidad de elementos después de eleminar el elemento: ', listUser.contador)
        for d in listUser.iterar():
            print(d)

        print()

        print('Insertando valores de la listUsera a partir de un índice:')
        print('Cantidad actual de elementos: %i' % listUser.contador)
        print('Contenido en la posición 2 antes de la modificación: ' ,listUser[1])
        user1.dni = '80580564'
        user1.name= "uam"
        listUser[1] = user1.dni,user1.name
        print('Contenido en la posición 2 después de la modificación: ', listUser[1])
   

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
        



