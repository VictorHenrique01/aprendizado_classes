
### **Exercício 2: Sistema de Login com Controle de Erros**
#Crie uma classe `Usuario` com os atributos:
#- `nome` (string)
#- `senha` (string)
#Adicione um método `autenticar` que verifica se o nome e a senha correspondem a 
#um par previamente cadastrado (por exemplo, nome: "admin", senha: "1234").  
#Implemente um programa que:
#1. Solicite ao usuário o nome e a senha para fazer login.
#2. Lance uma exceção do tipo `ValueError` caso o nome ou a senha estejam incorretos.
#3. Envolva o processo de login em um bloco `try-except` e mostre uma mensagem clara caso ocorra um erro.
#4. Dê ao usuário até **3 tentativas** antes de exibir a mensagem "Acesso bloqueado".

class Usuario:
    def __init__(self, nome, senha):
        self.nome = nome
        self.senha = senha

    def autenticar(self, nome, senha):
        try:
            resultado = self.nome = "admin" and self.senha = "1234"
            return resultado
        
        except ValueError:
            print("Dados incorretos")

        except Exception as e:
            print(f"Erro inesperado {e}")

print("Login do Usuário:")
while True:
    try:

        nome = input("Nome do usuário: ")
        senha = input("Senha do usuário: ")
        
        user = Usuario(nome, senha)
        resultado = user.autenticar(nome, senha)
        if resultado == resultado:
            print("Login realizado")
            break
        else:
            for tentativa

            