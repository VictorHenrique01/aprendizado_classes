#enviando valores que não são fixos por parâmetro no método construtor
class Professor:
    def __init__(self, nome, drt, contratacao, status, disciplina, carga_maxima):
            self.nome = nome
            self.drt = drt
            self.contratacao = contratacao
            self.status = status
            self.disciplina = disciplina
            self.carga_maxima = carga_maxima
#criando dois métodos
    def set_disciplina(self, disciplina): 
        self.disciplina = disciplina
    def set_carga_maxima(self, carga_max):
        self.carga_maxima = carga_max

#programa principal
p1 = Professor('Claudio', '123456', '17/08/1990', 'Titular', 'Matemática', 16)

print(p1.nome)      #Claudio
print(p1.drt)       #123456
print(p1.contratacao)   #17/08/1990
print(p1.status)        #Titular
print(p1.disciplina)    #Matemática
print(p1.carga_maxima)  #16

# Atualizando os atributos usando os métodos da classe
p1.set_disciplina('Física')
p1.set_carga_maxima(20)

print(p1.disciplina)   # Física
print(p1.carga_maxima) # 20




