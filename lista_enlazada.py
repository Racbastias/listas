class Nodo:
    
    def __init__(self, nombre, descripcion, sgte=None):
        self.nombre = nombre
        self.descripcion = descripcion
        self.sgte = sgte

class Lista:
    #lista inicial empieza vacía
    def __init__(self):
        self.primero = None
    
    #le agregamos una caja
    def add_nodo(self, nombre, descripcion):
        if self.primero is None:
            self.primero = Nodo(nombre, descripcion)
            return
        
        #si la lista tiene al menos un Nodo
        ultimo_nodo = self.primero
        while ultimo_nodo.sgte is not None:
            ultimo_nodo = ultimo_nodo.sgte
        ultimo_nodo.sgte = Nodo(nombre, descripcion)
        
    #determinar el largo de la lista
    def largo(self):
        #crear un contador de elementos
        if self.primero is None:
            return ('La lista está vacía')
        else:
            contador = 1
            ultimo_nodo = self.primero
            while ultimo_nodo.sgte is not None:
                ultimo_nodo = ultimo_nodo.sgte
                contador += 1
            return (f"La lista tiene {contador} elementos")
    
    #buscar un elemento de la lista
    def buscar(self,nombre):
        # nombre == ultimo_nodo.sgte.nombre
        ultimo_nodo = self.primero
        while ultimo_nodo.nombre is not nombre:
            ultimo_nodo = ultimo_nodo.sgte
        if nombre is None:
            return ('La pelicula ingresada no está en la lista')
        else:
            return (f"La pelicula tien cateroría {ultimo_nodo.descripcion}")
        pass
    #como agregar los nombres en orden alfabético?

peliculas = Lista()
peliculas.add_nodo('matrix', 'sci-fi')
peliculas.add_nodo('inception', 'sci-fi')
peliculas.add_nodo('misery', 'terror')
peliculas.add_nodo('nomad land', 'drama')
peliculas.add_nodo('titanic', 'romance drama terror')

import pdb; pdb.set_trace()

# equipo: Juan, Andrea, Yo