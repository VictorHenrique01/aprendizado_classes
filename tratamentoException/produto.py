### **Exercício 1: Cadastro de Produtos com Validação**
#Crie uma classe chamada `Produto` que tenha os seguintes atributos:
#- `nome` (string)
#- `preco` (float)
#- `quantidade` (int)
#Adicione um método `calcular_valor_total` que retorna o valor total do estoque (preço * quantidade).  
#Implemente um programa que:
#1. Peça ao usuário para informar o nome, preço e quantidade de um produto.
#2. Lance exceções nos seguintes casos:
#  - Se o preço ou a quantidade forem negativos, dispare um erro do tipo `ValueError`.
#  - Se o preço ou a quantidade não forem numéricos, dispare um erro do tipo `TypeError`.
#3. Capture essas exceções e exiba mensagens claras ao usuário, permitindo que ele tente novamente.

class Produto:
    def __init__(self, nome, preco, quantidade):
        self.nome = nome
        self.preco = preco
        self.quantidade = quantidade

    def calc_vt(self):

        try:
            resultado = self.preco * self.quantidade
            return resultado
        
        except ValueError:
            print("Valor negativo não é permitido")

        except TypeError:
            print("Os valores precisam ser numéricos")

        except Exception as e:
           # Tratamento genérico para outros erros
           print(f"Ocorreu um erro inesperado: {e}")


print("Calculando valor total do estoque: ")
while True:
   try:
       nome = input("Nome do produto: ")
       preco = int(input("Digite o preço do produto: "))
       quantidade = int(input("Digite a quantidade desse produto: "))

       produto = Produto(nome, preco, quantidade)
       resultado = produto.calc_vt(preco, quantidade)
       if resultado is not None:
           print(f"Resultado: {resultado}")
           break
   except ValueError:
       # Tratamento de erro para entradas inválidas no input
       print("Erro: Por favor, digite valores numéricos.")

    