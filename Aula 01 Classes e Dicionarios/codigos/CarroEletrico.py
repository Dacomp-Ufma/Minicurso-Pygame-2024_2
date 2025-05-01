# Classes - classe Carro elétrico, que herda de carro

from Carro import Carro

# 6 Atributos e 3 Métodos
class CarroEletrico(Carro):
    def __init__(self, cor, modelo, ano, marca, capacidadeBateria):
        super().__init__(cor, modelo, ano, marca)  # Chama o construtor da classe pai
        self.capacidadeBateria = capacidadeBateria

    def carregarBateria(self):
        print(f"{self.modelo} está carregando a bateria de {self.capacidadeBateria} kWh")
