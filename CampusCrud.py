class Campus:
    # Constructor
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


#algoritmo de ordenamiento 
def partition(campusList, start, end, compare_func):
    pivot = campusList[start]
    low = start + 1
    high = end

    while True:
        while low <= high and compare_func(campusList[high], pivot):
            high = high - 1

        while low <= high and not compare_func(campusList[low], pivot):
            low = low + 1

        if low <= high:
            campusList[low], campusList[high] = campusList[high], campusList[low]
        else:
            break

    campusList[start], campusList[high] = campusList[high], campusList[start]

    return high

def quick_sort(campusList, start, end, compare_func):
    if start >= end:
        return

    p = partition(campusList, start, end, compare_func)
    quick_sort(campusList, start, p-1, compare_func)
    quick_sort(campusList, p+1, end, compare_func)

campusList:list = []
campus1= Campus("800206234", "La Estrella", "312 6598765", "La Palma", "60")
#gym2 = Gym("900987652", "Muscle Center", "La Sultana", "311 9863572")

campusList.append(campus1)
#campusList.append(gym2)

quick_sort(campusList, 0, len(campusList) - 1, lambda x, y: x.nit < y.nit)
for Campus in campusList:
    print(Campus)


11






