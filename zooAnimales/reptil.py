from Animal import Animal

class Reptil(Animal):
    _listado=[]
    iguanas=0
    serpientes=0
    def __init__(self,nombre,edad,habitat,genero,colorEscamas,largoCola):
        super().__init__(nombre,edad,habitat,genero)
        self._colorEscamas=colorEscamas
        self._largoCola=largoCola
        Reptil._listado.append(self)
    
    def movimiento(self):
        return
    
    
    @classmethod
    def crearIguana(cls):
        cls.iguanas+=1
        
    @classmethod    
    def crearSerpiente(cls):
        cls.serpientes+=1
        
    
        
    @classmethod
    def cantidadReptiles(cls):
        return len(cls._listado)
    
    