#Crie uma classe Circulo com um atributo privado raio. 
#Use a propriedade property para criar getters e setters para o raio. 
#Além disso, adicione um método de propriedade area que calcule e 
#retorne a área do círculo (área = π * raio^2). Garanta que o raio não possa ser negativo.

class Circulo:
    def __init__(self, raio):
        self.raio = raio

    @property
    def raio(self):
        return self.__raio
    
    @raio.setter
    def raio(self, raio):
        if raio >= 0:
            self.__raio = raio
            print(f'Raio: {self.raio} | Área: {3.14 * self.raio ** 2} ')
        else:
            print('O valor do raio precisa ser positivo.')
    

            
circle = Circulo(-2)
