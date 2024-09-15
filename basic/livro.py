# 3. Sistema de Biblioteca. Descrição: Desenvolva uma classe Livro com atributos para título,
# autor, ano de publicação e disponibilidade. Adicione métodos para emprestar e devolver o livro,
# alterando seu status de disponibilidade.

class Livro:
    def __init__(self, titulo, autor, ano_publicacao, disponibilidade):
        self.titulo = titulo
        self.autor = autor
        self.ano_publicacao = ano_publicacao
        self.disponibilidade = disponibilidade
    
    def set_emprestar(self, disponibilidade):
        self.disponibilidade -= disponibilidade
    
    def set_devolver(self, disponibilidade):
        self.disponibilidade += disponibilidade

    def exibe_info(self):
        print(f'Título do livro: {self.titulo} | Autor: {self.autor} | Ano publicado: {self.ano_publicacao} | Quantos disponíveis? {self.disponibilidade}')

p1 = Livro(titulo= 'Metamorfose', autor= 'Franz Kafka', ano_publicacao= 2005, disponibilidade= 5)
print(p1.exibe_info())

p1.set_emprestar(3)
p1.exibe_info()
p1.set_devolver(3)
p1.exibe_info()