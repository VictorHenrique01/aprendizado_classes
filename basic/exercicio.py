#1. Controle de Estoque
#Descrição: Implemente uma classe Produto com atributos para nome, preço e quantidade em estoque. Adicione métodos para
#adicionar e remover produtos do estoque, e um método para imprimir as informações do produto.

class Produto:
    def __init__(self, nome, preco, quantidade):
        self.nome = nome
        self.preco = preco
        self.quantidade = quantidade
    
    def set_adicionar(self, quantidade):
        self.quantidade += quantidade
    def set_remover(self, quantidade):
        self.quantidade -= quantidade
    def imprimir(self):
        print(f"Nome: {self.nome}, Preço: {self.preco}, Quantidade: {self.quantidade}")

p1 = Produto(nome= 'Renner', preco= 20, quantidade= 8)
print(p1.imprimir())

p1.set_adicionar(5)
p1.imprimir()
p1.set_remover(3)
p1.imprimir()







        