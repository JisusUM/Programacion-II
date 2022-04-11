from enum import Enum
from datetime import date, datetime
#from Enums import ProductType
from typing import Any



class Product :
    def __init__(self, productId:int,productNombre:str,precio:float,marca:str,vencimiento:datetime,disponible:bool,proveedor:Any):
        self.productId:int= productId
        self.productNombre:str = productNombre
        self.precio:float = precio
        self.marca:str = marca
        self.vencimiento:datetime = vencimiento
        self.disponible:bool = disponible
        self.proveedor = proveedor
        

    def __str__(self):
        return f"Id Produc {str(self.productId)},Nombre {str(self.productNombre)},precio= {str(self.precio)}"
    def getProductNombre(self):
        return self.productNombre
    def getPrecio(self):
        return self.precio
    def setProductNombre(self,productNombre):
        self.productNombre = productNombre
    def setPrecio(self,precio):
        self.precio = precio
    def setMarca(self,marca):
        self.marca= marca
    def setVencimiento(self,vencimiento):
        self.vencimiento= vencimiento
    def setDisponible(self,disponible):
        self.disponible= disponible
    def setProveedor(self,proveedor):
        self.proveedor= proveedor

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

#algoritmo de ordenamiento 
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
    else:
        print("Opcion incorrecta")