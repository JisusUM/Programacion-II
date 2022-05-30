class Node(object):
    def __init__(self,item):
        self.item=item
        self.next=None
        self.prior=None

class DoubleLinkList(object):
    "" "Lista doblemente enlazada" ""
    def __init__(self,node=None): #Si no se pasa el nodo, el valor predeterminado es vacío
        self._head=node

    def is_empty(self):  # ¿Está vacía la lista vinculada?
        return self._head == None

    def length(self):   # Longitud de la lista de enlaces
        p = self._head  # p para mover el nodo transversal
        count = 0
        while (p != None):  #Si la condición del bucle es p.next! = None, hasta que se alcance el último nodo, la condición no se cumple y sale, no se puede contar el recuento
            count += 1
            p = p.next
        return count

    def travel(self):    # Recorre toda la lista vinculada
        p=self._head
        while(p!=None):
            print(p.item,end=' ')
            p=p.next

    def add(self,item):   #Añadir nodos a la cabeza
        node=Node(item)
        if self.is_empty():
            self._head=node
        else:
            node.next=self._head
            self._head.prior=node
            self._head=node

    def append(self,item):   #Añadir nodos a la cola
        node = Node(item)
        if self.is_empty():
            self._head=node
        else:
            p = self._head
            while(p.next!=None):
                p=p.next
            p.next=node
            node.prior=p
    def insert(self,pos,item): #Añadir nodo a cualquier posición
        if pos<=0:
            self.add(item)
        elif pos>(self.length()-1):
            self.append(item)
        else:
            p = self._head
            node = Node(item)
            count = 0
            while (count < pos):
                p = p.next
                count += 1
                # Cuando el bucle termina, p apunta a la posición de pos
                node.next = p
                node.prior=p.prior
                p.prior.next=node
                p.prior=node


    def remove(self,item):    # Eliminar un nodo
        p=self._head
        while(p!=None):  #Asegúrate de atravesar todos los nodos
            if p.elem == item:
                if p==self._head:
                    self._head=p.next
                    if p.next: # Juzgando que la lista enlazada tiene un solo nodo
                        p.next.prior=None
                else:
                    p.prior.next=p.next
                    if p.next:
                        p.next.prior=p.prior
                break
            else:
                p=p.next

    def search(self, item):
        "" "La lista vinculada busca si el nodo existe y devuelve Verdadero o Falso" ""
        p = self._head
        while p != None:
            if p.elem == item:
                return True
            p = p.next
        return False


if __name__ == '__main__':
    single_obj = DoubleLinkList()
    print(single_obj.is_empty() )
    single_obj.add(5)
    single_obj.add(6)
    single_obj.add(7)
    single_obj.travel()
