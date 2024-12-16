from gestion.zona import Zona
from gestion.zoologico import Zoologico 
from zooAnimales.anfibio import Anfibio
from zooAnimales.ave import Ave
from zooAnimales.mamifero import Mamifero
from zooAnimales.pez import Pez
from zooAnimales.reptil import Reptil

zoo = Zoologico("Zoologico Central", "Chicago")
z1 = Zona("zona1")
z2 = Zona("zona2")
zoo.agregarZonas(z1)
zoo.agregarZonas(z2)
z1.agregarAnimales(Mamifero.crearCaballo("test", 11, "M"))
z1.agregarAnimales(Mamifero.crearCaballo("test", 11, "M"))
z1.agregarAnimales(Mamifero.crearLeon("test", 11, "M"))

