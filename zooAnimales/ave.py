from .animal import Animal

class Ave(Animal):
    _listado = []
    halcones = 0
    aguilas = 0
    _colorPlumas = ''

    def __init__(self, nombre, edad, habitat, genero, colorPlumas):
        self._nombre = nombre
        self._edad = edad
        self._habitat = habitat
        self._genero = genero
        self._colorPlumas = colorPlumas
        Ave._listado.append(self)
        Animal.setTotalAnimales(Animal.getTotalAnimales() + 1)

    def getListado(self):
        return self._listado
    
    def setListado(self, L: list) -> None:
        self._listado = L

    def getColorPlumas(self):
        return self._colorPlumas
    
    def setColorPlumas(self, pe: bool) -> None:
        self._colorPlumas = pe

    def cantidadAves(self) -> int:
        return len(self._listado)

    @classmethod
    def crearHalcon(cls, nombre, edad, genero) -> Animal:
        cls._colorPlumas = 'cafe glorioso'
        cls.setHabitat(cls, 'montanas')
        return Ave(nombre, edad, cls.getHabitat(cls), genero, cls._pelaje, cls._patas)

    @classmethod
    def crearAguila(cls, nombre, edad, genero) -> Animal:
        cls._colorPlumas = 'blanco y amarillo'
        cls.setHabitat(cls, 'montanas')
        return Ave(nombre, edad, cls.getHabitat(cls), genero, cls._pelaje, cls._patas)

    def movimiento():
        return 'volar'
    
