#DuckTyping
class Duck:
    def fly(self):
        print("El pato vuela")
    def swim(self):
        print("El pato nada")
        
class Person:
    def fly(self):
        print("La persona vuela en avion")
    def swim(self):
        print("La persona nada en la piscina")
        
class Fish:
    def fly(self):
        print("El pez vuela mientras nada")
    def swim(self):
        print("El pez nada en el mar")
        
def flying_swiming(object):
    object.fly()
    object.swim()
    
Lucas = Duck()
Peter = Person()
Nemo = Fish()

flying_swiming(Lucas)
flying_swiming(Peter)
flying_swiming(Nemo)