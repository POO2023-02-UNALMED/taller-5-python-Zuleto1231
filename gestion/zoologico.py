class Zoologico:
    def __init__(self,nombre,ubicación):
        self._nombre=nombre
        self._ubicacion=ubicación
        self._zonas=[]
        
    def agregarZonas(self,zona):
        self._zonas.append(zona)
        
    def cantidadTotalAnimales(self):
        total=0
        for zona in self._zonas:
            total+=len(zona)
        return total
    
    
    def getNombre(self):
        return self._nombre
    
    def setNombre(self, nombre):
        self._nombre = nombre

    def getUbicacion(self):
        return self._ubicacion
    
    def setUbicacion(self, ubicacion):
        self._ubicacion = ubicacion

    @classmethod
    def getZona(cls):
        return cls._zonas
    
    @classmethod
    def setZona(cls, zonas):
        cls._zonas = zonas
            