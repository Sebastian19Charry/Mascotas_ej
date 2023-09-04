from tienda import *

t = Tienda()

t.agregar_animal(Perro("boxer",2,5))
t.agregar_animal(Perro("chihuahua",2,1))
t.agregar_animal(Gato("calico", 2, 0.5))
t.agregar_animal(Gato("persa", 2, 0.7))
t.agregar_animal(Gato("esfinge", 12, 1.5))
t.agregar_animal(Pez("golden", 0.5, 0.1))
t.agregar_animal(Pez("telescopio", 0.5, 0.01))
t.agregar_animal(Pez("coridora", 0.5, 0.01))
t.agregar_animal(Ave("loro", 1, 0.5))
t.agregar_animal(Ave("perico", 1, 0.5))
t.agregar_animal(Ave("cacatua", 1, 0.5))


for i in range(5):  
    a = t.entrgar_animal()
    print(a.saludar(), a.mostrar_informacion())