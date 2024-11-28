#Crie uma classe com um atributo privado  e um atributo público.
#Use um getter e um setter para, e adicione validação no setter para 
#garantir que a idade não seja negativa. Se uma idade negativa for passada, 
#defina a idade como 0 e imprima uma mensagem de aviso.

class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    @property
    def idade(self):
        return self.__idade
    
    @idade.setter
    def idade(self, idade):
        if idade >= 0:
            self.__idade = idade
        else:
            self.__idade = 0
            print('Idade inválida! \nDefinindo como 0...')
    
    def exibir(self):
        print(f'Nome: {self.nome} | Idade: {self.idade}')

pessoa1 = Pessoa('Victor', 18)
pessoa1.exibir()
