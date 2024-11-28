#Exercício 6: Associação Simples
#Crie uma classe Professor e uma classe Disciplina. Um professor pode estar associado a várias disciplinas,
#mas essa associação não implica em um relacionamento forte onde a existência da disciplina 
#depende do professor. A relação deve ser uma associação simples.
#• Defina a classe lista de com um atributo e uma Disciplina

class Disciplina:
   def __init__(self, nome):
       self.nome = nome  


class Professor:
   def __init__(self, nome):
       self.nome = nome  
       self.disciplinas = []  # Lista de disciplinas doo professor
   def adicionar_disciplina(self, disciplina):
       """Adiciona uma disciplina à lista de disciplinas do professor"""
       self.disciplinas.append(disciplina)
   def listar_disciplinas(self):
       """Lista os nomes das disciplinas associadas ao professor"""
       return [disciplina.nome for disciplina in self.disciplinas]
   def __str__(self):
       return self.nome 

if __name__ == "__main__":

   matematica = Disciplina("Matemática")
   fisica = Disciplina("Física")
   quimica = Disciplina("Química")

   professor1 = Professor("Dr. João")
   professor1.adicionar_disciplina(matematica)
   professor1.adicionar_disciplina(fisica)

   print(f"Professor: {professor1}")
   print("Disciplinas associadas:")
   for disciplina in professor1.listar_disciplinas():
       print(f"- {disciplina}")

   professor2 = Professor("Prof. Maria")
   professor2.adicionar_disciplina(quimica)
   print(f"\nProfessor: {professor2}")
   print("Disciplinas associadas:")
   for disciplina in professor2.listar_disciplinas():
       print(f"- {disciplina}")