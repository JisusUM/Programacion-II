class Campus:
    # Constructor ###
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







