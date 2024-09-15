# Descrição: Implemente uma classe Carro com atributos para marca, modelo, ano e quilometragem.
# Inclua métodos para dirigir o carro, que aumenta a quilometragem, e outro método
# para exibir informações do carro.

class Carro:
    def __init__(self, marca, modelo, ano, quilometragem):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.quilometragem = quilometragem
    
    def exibe_info(self):
        print(f'Marca do carro: {self.marca} | Modelo: {self.modelo} | Ano: {self.ano} | Km: {self.quilometragem}')

    def dirigir_carro(self, quilometragem):
        self.quilometragem += quilometragem

p1 = Carro(marca= 'Ferrari', modelo='FERRARI F8 SPIDER', ano= 2022, quilometragem= 300)
print(p1.exibe_info())

p1.dirigir_carro(50)
p1.exibe_info()