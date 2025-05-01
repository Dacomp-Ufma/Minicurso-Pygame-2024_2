# Classes - classe carro, que define uma abstração de um carro em forma de classe 

# 4 Atributos e 2 Métodos
class Carro:
    def __init__(self, cor, modelo, ano, marca):
        self.cor = cor
        self.modelo = modelo
        self.ano = ano
        self.marca = marca


    def acelerar(self):
            print(f"{self.modelo} está acelerando")

    def frear(self):
            print(f"{self.modelo} está freando")