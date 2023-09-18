from Animal import Animal

class Ave(Animal):
    _listado=[]
    halcones=0
    aguilas=0
    def __init__(self,nombre,edad,habitat,genero,colorPlumas):
        super().__init__(nombre,edad,habitat,genero)
        self._colorPlumas=colorPlumas
        Ave._listado.append(self)
    
    def movimiento(self):
        return
    
    
    @classmethod
    def crearHalcones(cls):
        cls.halcones+=1
        
    @classmethod    
    def crearAguilas(cls):
        cls.aguilas+=1
        
    
        
    @classmethod
    def cantidadAves(cls):
        return len(cls._listado)
    
    