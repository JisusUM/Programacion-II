
# Crear clase Gym
class Gym:
    # Constructor
    def __init__(self, nit:int, name:str, address:str, phone:str):
        # Datos de entrada
        self._nit:int = nit
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

