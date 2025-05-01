# Classes - Usando as classes criadas durante a aula

from Carro import Carro
from CarroEletrico import CarroEletrico

carro1 = Carro("verde", "New Beetle", 2007, "volkswagen")
carro2 = Carro("azul", "miata", 2015, "mazda")
carro3 = CarroEletrico("preto", "carro", 2025, "marca", 100)


print(carro1.cor)
print(carro2.cor)

carro1.acelerar()
carro3.carregarBateria()