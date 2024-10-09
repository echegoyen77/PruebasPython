class Empleado():
    def __init__(self, nombre, cedula, telefono):
        self._nombre = nombre
        self._cedula = cedula
        self._telefono = telefono
        
    def getNombre(self):
        return self._nombre
        
    def getCedula(self):
        return self._cedula         
        
    def getTelefono(self):
        return self._telefono
        
    def setNombre(self, nombre):
        self_nombre = nombre        
        
    def setCedula(self, cedula):
        self_cedula = cedula        
        
    def setTelefono(self, telefono):
        self_telefono = telefono        
    
    
class EmpleadoDefinido(Empleado):
    def __init__(self, nombre, cedula, telefono, numeroPlaza, salario, duracion):
        super().__init__(nombre, cedula, telefono)
        self._numeroPlaza = numeroPlaza
        self._salario = salario
        self._duracion = duracion
        
    def getNumberoPlaza(self):
        return self._numeroPlaza
        
    def getSalario(self):
        return self._salario         
        
    def getDuracion(self):
        return self.duracion
        
    def setNumeroPlaza(self, numeroPlaza):
        self._numeroPlaza = numeroPlaza        
        
    def setSalario(self, salario):
        self._salario = salario        
        
    def setDuracion(self, duracion):
        self._duracion = duracion 
        
    def salarioTotal(self):
        return self._salario + (self._salario * 0.02)
    

class EmpleadoIndefinido(Empleado):
    def __init__(self, nombre, cedula, telefono, numeroPlaza, salario, categoria):
        super().__init__(nombre, cedula, telefono)
        self._numeroPlaza = numeroPlaza
        self._salario = salario
        self._categoria = categoria
        
    def getNumberoPlaza(self):
        return self._numeroPlaza
        
    def getSalario(self):
        return self._salario         
        
    def getCategoria(self):
        return self.categoria
        
    def setNumeroPlaza(self, numeroPlaza):
        self._numeroPlaza = numeroPlaza        
        
    def setSalario(self, salario):
        self._salario = salario        
        
    def setCategoria(self, categoria):
        self._categoria = categoria 
        
    def salarioTotal(self, categoria):
        salarioFinal = 0
        
        match categoria:
            case 1:
                return self._salario + (self._salario * 0.03) 
            case 2: 
                return self._salario + (self._salario * 0.05) 
            case 3:  
                return self._salario + (self._salario * 0.08) 
            case _:
                return self._salario