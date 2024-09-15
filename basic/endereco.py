# 2. Gerenciamento de Pessoas. Descrição: Crie uma classe Pessoa com atributos para nome,
# idade e endereço. Inclua métodos para alterar o endereço e
# outro para exibir todas as informações da pessoa.

class Pessoa:
    def __init__(self, nome, idade, endereco):
        self.nome = nome
        self.idade = idade
        self.endereco = endereco
    
    def exibe_info(self):
        print(f'Nome: {self.nome} | Quantos anos? {self.idade} | Seu endereço: {self.endereco}')

    def altera_end(self, endereco):
        self.endereco = endereco

p1 = Pessoa(nome= 'Victor', idade= 18, endereco= 'Rua alonso berruguete, 104')
print(p1.exibe_info())

p1.altera_end('Rua Alberto Andaló, 87')
p1.exibe_info()
        