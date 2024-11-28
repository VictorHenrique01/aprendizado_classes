### **1. Exercício Básico: Atributos e Métodos**
#Crie uma classe chamada `Cachorro` que tenha os seguintes atributos:
#- `nome` (nome do cachorro),
#- `idade` (idade do cachorro, em anos),
#- `raça` (raça do cachorro).
#A classe deve ter um método chamado `latir()` que exibe a mensagem:
#`"Au au! Meu nome é {nome}!"`, onde `{nome}` deve ser substituído pelo nome do cachorro.
#**Tarefa**  
#Crie uma instância da classe `Cachorro` e chame o método `latir()` 
#para exibir a mensagem. Além disso, exiba no terminal os atributos do objeto criado

class Cachorro:
    def __init__(self, nome, idade, raca):
        self.nome = nome
        self.idade = idade
        self.raca = raca

    def latir(self):
        print(f'Au au! Meu nome é {self.nome}, tenho {self.idade} anos e sou da raça {self.raca}')

cao = Cachorro("Lion", 4, "Golden")
cao.latir()

