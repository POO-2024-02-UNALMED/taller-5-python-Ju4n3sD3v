from animal import Animal
class Mamifero(Animal):
    _listado = []
    caballos = 0
    leones = 0
    _pelaje = True
    _patas = 4

    def __init__(self, nombre, edad, habitat, genero, pelaje, patas):
        super().__init__(nombre, edad, habitat, genero)
        self._pelaje = pelaje
        self._patas = patas

    def getListado(self):
        return self._listado
    
    def setListado(self, L: list) -> None:
        self._listado = L

    def getPelaje(self):
        return self._pelaje
    
    def setPelaje(self, pe: bool) -> None:
        self._pelaje = pe

    def getPatas(self):
        return self._patas
    
    def setPatas(self, pa: int) -> None:
        self._patas = pa

    def cantidadMamiferos(self) -> int:
        pass

    def crearCaballo(self) -> Animal:
        pass

    def crearLeon(self) -> Animal:
        pass