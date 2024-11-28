#Crie uma classe chamada Veiculo com os atributos marca, modelo e o 
#método informar_dados() que exibe essas informações.
#Depois, crie duas classes que herdam de Veiculo: Carro e Moto.
#Adicione um atributo específico em cada classe 
#(por exemplo, quantidade_de_portas no Carro e tipo_de_guidao na Moto) 
#e ajuste o método informar_dados() para incluir esses detalhes.

class Veiculo:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

    def exibe(self):
        print(f'Carro da marca {self.marca} | modelo: {self.modelo}')

class Carro(Veiculo):
    def __init__(self, marca, modelo, qtd_portas):
        super().__init__(marca, modelo)
        self.qtd_portas = qtd_portas

    def exibe(self):
        super().exibe()
        print(f'Quantidade de portas: {self.qtd_portas}')

class Moto(Veiculo):
    def __init__(self, marca, modelo, tipo_guidao):
        super().__init__(marca, modelo)
        self.tipo_guidao = tipo_guidao

    def exibe(self):
        super().exibe()
        print(f'Tipo do guidão: {self.tipo_guidao}')

v1 = Veiculo('Auge', 'Q7')
v1.exibe()
print("----------------------------------------------------")
c1 = Carro('Fiat', 'Argo', 4)
c1.exibe()
print("----------------------------------------------------")
m1 = Moto('Hornet', 'Das braba', 'Esportivo')
m1.exibe()