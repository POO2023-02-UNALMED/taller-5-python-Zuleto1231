class Zona:
    def __init__(self,nombre,zoologico=None):
        self._nombre=nombre
        self._zoologico=zoologico
        self._animales=[]
        
    def agregarAnimales(self,animal):
        self._animales.append(animal)
        
    def cantidadAnimales(self):
        return len(self._animales)
    
    def setNombre (self, nombre):
        self._nombre = nombre

    def getNombre (self):
        return self._nombre
    
    def getZoo(self):
        return self._zoologico
    
    def setZoo(self, zoo):
        self._zoologico = zoo
        
        