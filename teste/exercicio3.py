### **3. Exercício: Atributos Privados com `property`**
#**Enunciado**  
#Crie uma classe chamada `ContaBancaria` com:
#- Um atributo privado chamado `_saldo` que inicia com o valor 0.
#- Um método chamado `depositar(valor)` que adiciona o valor ao saldo, 
#desde que o valor seja positivo.
#- Um método chamado `sacar(valor)` que reduz o saldo, 
#desde que o valor seja positivo e o saldo seja suficiente.
#Utilize a propriedade `@property` para criar os métodos `get_saldo()` (para acessar o saldo) e 
#`set_saldo()` (para alterar o saldo, garantindo que ele nunca seja negativo).
#**Tarefa**  
#Crie uma instância da classe `ContaBancaria`. Realize depósitos, saques e exiba o saldo atual
#usando a propriedade.

class ContaBancaria:
    def __init__(self, saldo):
        self.saldo = saldo

    @property
    def saldo(self):
        return self.__saldo
    
    @saldo.setter
    def saldo(self, saldo):
        if saldo >= 0:
            self.__saldo = saldo
        else:
            self.__saldo = 0
            print('Saldo não deve ser negativo! \nDefinindo como 0...')

    def depositar(self, valor):
        if valor >= 0:
            valor = self.__saldo + valor
            return valor
        else:
            ("Depósito não pode ser negativo.")
    
    def sacar(self, valor):
        valor = self.__saldo - valor
        return valor
    
    def exibir(self):
        print(f"Saldo em conta corrente atualmente: {self.__saldo}")

    
conta = ContaBancaria(1000.00)
print(conta.depositar(-50))
conta.exibir()


    



