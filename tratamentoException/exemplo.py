### **Exemplo: Calculadora Simples com Validação**
#Neste exemplo, criamos uma pequena aplicação para calcular 
#a divisão entre dois números, com tratamento de exceções.
#### Código:

class Calculadora:
   def __init__(self):
       pass
   def dividir(self, numerador, denominador):
       try:
           # Tentativa de realizar a divisão
           resultado = numerador / denominador
           return resultado
       except ZeroDivisionError:
           # Tratamento para divisão por zero
           print("Erro: Não é possível dividir por zero.")
       except TypeError:
           # Tratamento para entrada de dados não numérica
           print("Erro: Os valores precisam ser números.")
       except Exception as e:
           # Tratamento genérico para outros erros
           print(f"Ocorreu um erro inesperado: {e}")
# Programa principal
print("Calculadora de divisão")
while True:
   try:
       # Solicita ao usuário dois números
       numerador = float(input("Digite o numerador: "))
       denominador = float(input("Digite o denominador: "))
       # Cria uma instância da calculadora
       calc = Calculadora()
       resultado = calc.dividir(numerador, denominador)
       # Verifica se a divisão foi bem-sucedida
       if resultado is not None:
           print(f"Resultado: {resultado}")
           break
   except ValueError:
       # Tratamento de erro para entradas inválidas no input
       print("Erro: Por favor, digite valores numéricos.")

### **Explicação detalhada**:
#1. **Classe Calculadora**:
 # - Criamos uma classe `Calculadora` que possui um método chamado `dividir`.
  #- Esse método tenta dividir dois números e trata possíveis erros usando um bloco `try-except`.

#2. **Bloco try-except no método `dividir`**:
 # - **`ZeroDivisionError`**: Tratamos o caso em que o denominador é zero, exibindo
 #  uma mensagem para o usuário.
 #- **`TypeError`**: Lidamos com situações em que os valores fornecidos não são numéricos 
 # (embora isso já seja capturado no `try` do programa principal neste caso).
 #- **`Exception`**: Captura outros erros inesperados, exibindo o erro original 
 # para facilitar a depuração.

#3. **Bloco try-except no programa principal**:
#  - Solicitamos entrada do usuário para os números.
#  - Caso o usuário insira valores inválidos (por exemplo, letras ou símbolos), 
# usamos um `ValueError` para capturar e exibir uma mensagem de erro.

#4. **Laço `while`**:
#  - O programa permite que o usuário tente novamente em caso de erro, até que 
# uma divisão válida seja realizada.


### **O que acontece ao executar o código?**
#- O programa solicita ao usuário dois números para realizar a divisão.
#- Se houver algum erro (como tentar dividir por zero ou inserir letras),
#  uma mensagem clara será exibida, e o usuário poderá tentar novamente.

#- Ao final, caso a divisão seja bem-sucedida, o programa exibe o resultado e finaliza.
### **Saída Esperada**:
#### Caso 1: Divisão por zero
