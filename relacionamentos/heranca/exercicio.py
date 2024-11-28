#Crie uma classe chamada Pessoa com os atributos nome e idade, além de um método apresentar() 
#que imprime o nome e a idade da pessoa.
#Depois, crie uma classe Aluno que herda de Pessoa e adicione o atributo curso.
#Na classe Aluno, sobrescreva o método apresentar() para incluir também o curso do aluno.

class Pessoa:
    def __init__ (self, nome, idade):
        self.nome = nome
        self.idade = idade

    def apresentar(self):
        print(f'Nome da pessoa: {self.nome} | Idade: {self.idade}')
    

class Aluno(Pessoa):
    def __init__(self, nome, idade, curso):
        super().__init__(nome, idade)
        self.curso = curso

    def apresentar(self):
        super().apresentar()
        print(f'Curso: {self.curso}')
    
    
p1 = Pessoa('Julia', 17)   
p1.apresentar()
print("-----------------------------------")
aluno1 = Aluno('Victor', 19, 'ADS')
aluno1.apresentar()
