# 6. Controle de Animais de Estimação. Descrição: Desenvolva uma classe AnimalDeEstimacao com
# atributos para nome, espécie e idade. Inclua métodos para alterar a idade do animal
# e outro para exibir as informações do animal.

class AnimalDeEstimacao:
    def __init__(self, nome, especie, idade):
        self.nome = nome
        self.especie = especie
        self.idade = idade
    
    def exibe_info(self):
        print(f'Nome do animal: {self.nome} | Espécie: {self.especie} | Idade: {self.idade} anos')

    def altera_idade(self, idade):
        self.idade = idade

p1 = AnimalDeEstimacao('Cachorro', 'Pitbull', 5)
print(p1.exibe_info())

p1.altera_idade(3)
p1.exibe_info()