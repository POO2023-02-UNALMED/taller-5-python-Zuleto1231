
class Animal:
    _totalAnimales=0
    def __init__(self,nombre,edad,habitat,genero):
        self._nombre=nombre
        self._edad=edad
        self._habitat=habitat
        self._genero=genero
        self._zona=None
        Animal._totalAnimales+=1
        
    def movimiento(self):
        return
        
    def totalPortipo(self):
        from mamifero import Mamifero
        from reptil import Reptil
        from ave import Ave
        from pez import Pez
        from anfibio import Anfibio
        
        return ("Mamiferos: "+ str(Mamifero.cantidadMamiferos)+
                "\nAves: " + str(Ave.cantidadAves)+
                "\nReptiles: " + str(Reptil.cantidadReptiles)+
                "\nPeces: " + str(Pez.cantidadPeces)+
                "\nAnfibios: " + str(Anfibio.cantidadAnfibios) )

        
    def __str__(self):
        if self._zona != None:
            return ("Mi nombre es " + self._nombre +
                ", tengo una edad de " + str(self._edad) +
                ", habito en " + self._habitat +
                " y mi genero es " + self._genero +
                ", la zona en la que me ubico es " + self._zona +
                ", en el " + self._zona._zoologico._nombre)
        else:
            return ("Mi nombre es " + self._nombre +
                ", tengo una edad de " + str(self._edad) +
                ", habito en " + self._habitat +
                " y mi genero es " + self._genero)

        
        