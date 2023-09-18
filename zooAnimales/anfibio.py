from Animal import Animal

class Anfibio(Animal):
    _listado=[]
    ranas=0
    salamandras=0
    def __init__(self,nombre,edad,habitat,genero,colorPiel,venenoso):
        super().__init__(nombre,edad,habitat,genero)
        self._colorPiel=colorPiel
        self._venenoso=venenoso
        Anfibio._listado.append(self)
    
    def movimiento(self):
        return
    @classmethod
    def crearRana(cls):
        cls.ranas+=1
        
    @classmethod    
    def crearSalamandra(cls):
        cls.salamandras+=1
    
        
    @classmethod
    def cantidadAnfibios(cls):
        return len(cls._listado)
    
    
    