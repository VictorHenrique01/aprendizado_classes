#Novo Exercício 2: Herança com Sobrecarga
#Enunciado
#Crie uma classe chamada Funcionario com os seguintes atributos:
#• nome (nome do funcionário),
#• salario (salário do funcionário).
#A classe deve ter um método chamado exibir_dados() que exibe o nome e o salário do funcionário.
#Crie uma classe chamada Gerente que herda de Funcionario.
#A classe Gerente deve adicionar o atributo:
#• bonus (bônus salarial do gerente).
#Sobrescreva o método exibir_dados() para exibir o nome, o salário e o bônus do gerente.
#Tarefa
#• Crie uma instância da classe Funcionario e outra da classe Gerente.
#• Exiba os dados de cada objeto utilizando o método exibir_dados().

class Funcionario:
    def __init__(self, nome, salario):
        self.nome = nome
        self.salario = salario

    def exibir(self):
        print(f'- Dados do funcionário \nNome: {self.nome} | Salário: {self.salario}')

class Gerente(Funcionario):
    def __init__(self, nome, salario, bonus):
        super().__init__(nome, salario)
        self.bonus = bonus

    def exibir(self):
        super().exibir()
        print(f"Bônus do gerente: {self.bonus} ")

f1 = Funcionario("Léo", 3000.00)
f1.exibir()
print("---------------------------------------")
g1 = Gerente("Victor", 10000.00, 2200.00)
g1.exibir()