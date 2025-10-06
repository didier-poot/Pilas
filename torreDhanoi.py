from Pila import pila

def moverDisco(torreOrigen, torreDestino):
    disco = torreOrigen.pop()   
    if disco == "La pila está vacía":
        return
    torreDestino.push(disco)

def juegoHanoi(n, torreOrigen, torreAuxiliar, torreDestino):
    if n == 1:
        moverDisco(torreOrigen, torreDestino)
    else:
        juegoHanoi(n-1, torreOrigen, torreDestino, torreAuxiliar)
        moverDisco(torreOrigen, torreDestino)
        juegoHanoi(n-1, torreAuxiliar, torreOrigen, torreDestino)

Torre1 = pila()
Torre2 = pila()
Torre3 = pila()

for i in range(3, 0, -1):
    Torre1.push(i)

juegoHanoi(3, Torre1, Torre2, Torre3)

print("Torre 1:", Torre1.pila)
print("Torre 2:", Torre2.pila)
print("Torre 3:", Torre3.pila)
