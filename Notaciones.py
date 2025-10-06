import Pila
letras = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
numeros = ['0','1','2','3','4','5','6','7','8','9']
def formatear(expresion: str):
    exp = expresion.replace(" ","")
    return list(exp)
    
def infijo_A_postfijo (expresion : str):
    listaOperadores = {"*":3,"/":3,"+":2,"-":2,"(":1,}
    expresionPostfija = []
    pilaOperadores = Pila.pila()
    listaSimbolos = formatear(expresion)
    
    for caracter in listaSimbolos:
    
        if caracter in letras or caracter in numeros:
            expresionPostfija.append(caracter)
            
        elif caracter == '(':
            pilaOperadores.push(caracter)
        
        elif caracter == ')':
            final = pilaOperadores.pop()
            while final != '(':
                expresionPostfija.append(final)
                final = pilaOperadores.pop()
        else:
            while (not pilaOperadores.isempty() and listaOperadores[pilaOperadores.peek()] >= listaOperadores[caracter]):
                expresionPostfija.append(pilaOperadores.pop())
            pilaOperadores.push(caracter)
    
    while not pilaOperadores.isempty():
        expresionPostfija.append(pilaOperadores.pop())
    
    return expresionPostfija

def infijo_A_prefijo(expresion: str):
    prioridad = {"*":3, "/":3, "+":2, "-":2, "(":1}
    expresion = expresion[::-1]
    expresion = expresion.replace('(', 'temporal').replace(')', '(').replace('temporal', ')')
    pilaOperadores = Pila.pila()
    expresionPrefija = []
    for caracter in expresion:
        if caracter in letras or caracter in numeros:
            expresionPrefija.append(caracter)
        elif caracter == '(':
            pilaOperadores.push(caracter)
        elif caracter == ')':
            fin = pilaOperadores.pop()
            while fin != '(':
                expresionPrefija.append(fin)
                fin = pilaOperadores.pop()
        else:
            while (not pilaOperadores.isempty() and prioridad[pilaOperadores.peek()] > prioridad[caracter]):
                expresionPrefija.append(pilaOperadores.pop())
            pilaOperadores.push(caracter)

    while not pilaOperadores.isempty():
        expresionPrefija.append(pilaOperadores.pop())

    expresionPrefija.reverse()

    return expresionPrefija

Operaciones = str(input("Dame la expresión a convertir: "))
print("".join(infijo_A_prefijo(Operaciones)))