# 5. Registro de Alunos. Descrição: Crie uma classe Aluno com atributos para nome, matrícula e curso.
# Adicione métodos para mudar o curso do aluno e outro para exibir as informações do aluno.

class Alunos:
    def __init__(self, nome, matricula, curso):
        self.nome = nome
        self.matricula = matricula
        self.curso = curso

    def exibe_info(self):
        print(f'Nome: {self.nome} | Matrícula: {self.matricula} | Curso: {self.curso}')

    def altera(self, curso):
        self.curso = curso

p1 = Alunos('Victor Henrique', 2401280, 'Análise e desenvolvimento de sistemas')
print(p1.exibe_info())

p1.altera('Banco de Dados')
p1.exibe_info()    