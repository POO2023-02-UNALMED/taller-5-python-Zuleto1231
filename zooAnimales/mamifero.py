from Animal import Animal

class Mamifero(Animal):
    _listado=[]
    caballos=0
    leones=0
    def __init__(self,nombre,edad,habitat,genero,pelaje,patas):
        super().__init__(nombre,edad,habitat,genero)
        self._pelaje=pelaje
        self._patas=patas
        Mamifero._listado.append(self)
    
    def movimiento(self):
        return
    
    
    @classmethod
    def crearCaballos(cls):
        cls.caballos+=1
        
    @classmethod    
    def crearLeones(cls):
        cls.leones+=1
        
    
        
    @classmethod
    def cantidadAves(cls):
        return len(cls._listado)
    
    