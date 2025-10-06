from Pila import pila

def mostrar_estado(torreA, torreB, torreC):
    print("A:", torreA.pila)
    print("B:", torreB.pila)
    print("C:", torreC.pila)
    print("-" * 25)

def mover_disco(origen, destino, nombre_origen, nombre_destino):
    disco = origen.pop()
    if disco == "La pila está vacía":
        return
    destino.push(disco)
    print(f"Mover disco {disco} de {nombre_origen} → {nombre_destino}")
    mostrar_estado(torreA, torreB, torreC)

def hanoi(n, origen, auxiliar, destino, nombre_origen, nombre_aux, nombre_dest):
    if n == 1:
        mover_disco(origen, destino, nombre_origen, nombre_dest)
    else:
        hanoi(n - 1, origen, destino, auxiliar, nombre_origen, nombre_dest, nombre_aux)
        mover_disco(origen, destino, nombre_origen, nombre_dest)
        hanoi(n - 1, auxiliar, origen, destino, nombre_aux, nombre_origen, nombre_dest)

# Crear las tres torres usando tu clase pila
torreA = pila()
torreB = pila()
torreC = pila()

# Colocar los discos en la torre A (de mayor a menor)
for disco in range(3, 0, -1):
    torreA.push(disco)

print("Estado inicial:")
mostrar_estado(torreA, torreB, torreC)

# Resolver para 3 discos
print("Resolviendo Torres de Hanói con 3 discos...\n")
hanoi(3, torreA, torreB, torreC, "A", "B", "C")

print("✅ ¡Completado!")
mostrar_estado(torreA, torreB, torreC)
