# Crear clase Gym
class Gym:
    # Constructor
    def __init__(self, nit:str, name:str, address:str, phone:str):
        # Datos de entrada
        self._nit:str = nit
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

#algoritmo de ordenamiento 
def partition(gymList, start, end, compare_func):
    pivot = gymList[start]
    low = start + 1
    high = end

    while True:
        while low <= high and compare_func(gymList[high], pivot):
            high = high - 1

        while low <= high and not compare_func(gymList[low], pivot):
            low = low + 1

        if low <= high:
            gymList[low], gymList[high] = gymList[high], gymList[low]
        else:
            break

    gymList[start], gymList[high] = gymList[high], gymList[start]

    return high

def quick_sort(gymList, start, end, compare_func):
    if start >= end:
        return

    p = partition(gymList, start, end, compare_func)
    quick_sort(gymList, start, p-1, compare_func)
    quick_sort(gymList, p+1, end, compare_func)

gymList = []
gym1 = Gym("900712192", "European Hardcore", "Chipre", "311 6987561")
gym2 = Gym("900987652", "Muscle Center", "La Sultana", "311 9863572")



gymList.append(gym1)
gymList.append(gym2)

quick_sort(gymList, 0, len(gymList) - 1, lambda x, y: x.nit < y.nit)
for Gym in gymList:
    print(Gym)


