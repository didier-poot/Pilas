def pilaVacia():
    return "La pila esta vacia"

class pila:
    def __init__(self):
        self.pila = []
        
    def isempty(self):
        return len(self.pila)==0
        
    def push (self,elemento):
        self.pila.append(elemento)
        
    def pop (self):
        if self.isempty():
            return pilaVacia()
        
        return self.pila.pop()
    
    def peek (self):
        if self.isempty():
            return pilaVacia()
        
        return self.pila[-1]
        
    def size (self):
        return(len(self.pila))
    
    def vaciar(self):
        self.pila.clear()