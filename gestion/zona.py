class Zona:
    def __init__(self,nombre):
        self._nombre=nombre
        self._zoologico=None
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
        return self._zoo
    
    def setZoo(self, zoo):
        self._zoo = zoo
        
        