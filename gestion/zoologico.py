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
            