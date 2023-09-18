from gestion.zona import Zona
from gestion.zoologico import Zoologico 
from zooAnimales.anfibio import Anfibio
from zooAnimales.ave import Ave
from zooAnimales.mamifero import Mamifero
from zooAnimales.pez import Pez
from zooAnimales.reptil import Reptil
from zooAnimales.animal import Animal




Anfibio.crearRana("test", 11, "M")
Anfibio.crearSalamandra("test", 11, "M")
Mamifero.crearCaballo("test", 11, "M")
Mamifero.crearCaballo("test", 11, "M")
Mamifero.crearLeon("test", 11, "M")
Reptil.crearIguana("test", 11, "M")
Pez.crearSalmon("test", 11, "M")
Ave.crearHalcon("test", 11, "M")
Ave.crearHalcon("test", 11, "M")
ok = False
comp = "Mamiferos : 3\nAves : 2\nReptiles : 1\nPeces : 1\nAnfibios : 2"
print(comp.replace('\n', ''))
print(Animal.totalPorTipo().replace('\n', ''))