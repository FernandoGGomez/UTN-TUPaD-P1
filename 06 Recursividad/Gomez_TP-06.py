#1) Crea una función recursiva que calcule el factorial de un número. Luego, utiliza esa
# función para calcular y mostrar en pantalla el factorial de todos los números enteros
# entre 1 y el número que indique el usuario

def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n - 1)


numero = int(input("Ingrese un número para conocer su factorial y el de todos los números enteros entre 1 y ese número: "))

if numero <= 0:
    print(f"No se puede obtener el factorial de {numero}")
else:
    for i in range(1, numero + 1):
        print(f"El factorial del número {i} es: {factorial(i)}")


#2) Crea una función recursiva que calcule el valor de la serie de Fibonacci en la posición
#indicada. Posteriormente, muestra la serie completa hasta la posición que el usuario
#especifique.

def valor_Fibonacci(posicion):
    if posicion == 0:
        return 0
    elif posicion == 1:
        return 1
    else:
        valor = valor_Fibonacci(posicion - 1) + valor_Fibonacci(posicion - 2) 
        return valor
    
posicion = int(input("Ingrese la posición hasta la que quiere ver la serie de Fibonacci: "))

for i in range(0,posicion + 1):
    print(f"Posición {i} valor {valor_Fibonacci(i)}")




#3) Crea una función recursiva que calcule la potencia de un número base elevado a un
# exponente, utilizando la fórmula 𝑛𝑚 = 𝑛 ∗ 𝑛(𝑚−1). Prueba esta función en un
# algoritmo general.

def potencia(n,m):
    if m == 0:
        return 1
    else:
        return n * potencia(n,m - 1)
    
print("Potencia de 2 elevado a la 4:",potencia(2,4))


#4) Crear una función recursiva en Python que reciba un número entero positivo en base
#decimal y devuelva su representación en binario como una cadena de texto.

def decimal_a_binario(n):
    if n == 1:
        return "1" 
    elif n == 0:
        return "0" 
    else:
        return decimal_a_binario(n // 2) + str(n % 2)
         

num_decimal = int(input("Ingrese un número decimal entero y positivo para convertirlo en binario: "))
if num_decimal <= 0:
    print(f"El número {num_decimal} no es un entero positivo")
else:
    print(f"El número {num_decimal} en binario es: {decimal_a_binario(num_decimal)}")

#5) Implementá una función recursiva llamada es_palindromo(palabra) que reciba una
#cadena de texto sin espacios ni tildes, y devuelva True si es un palíndromo o False si no
#lo es.

def es_palindromo(palabra):
    if len(palabra) <= 1:
        return True
    #Si la primera y la última letra de la palabra son diferentes es porque no es un palíndromo
    elif palabra[0] != palabra[-1]:
        return False
    else:
        return es_palindromo(palabra[1:-1])

palabra = input("Ingrese una palabra para saber si es un palíndromo: ")
if es_palindromo(palabra):
    print(f"La palabra {palabra} es un palíndromo")
else:
    print(f"La palabra {palabra} no es un palíndromo")


#6) Escribí una función recursiva en Python llamada suma_digitos(n) que reciba un
#número entero positivo y devuelva la suma de todos sus dígitos.

def suma_digitos(n):
    if n == 0:
        return 0
    else:
        # con el módulo de 10 obtengo el último dígito del número
        digito = n % 10
        #Dividiendo el número por 10 le quito su último dígito
        n = n // 10
        return digito + suma_digitos(n)

numero = int(input("Ingrese un número para obtener la suma de todos sus dígitos: "))    
print(f"La suma de los dígitos de {numero} es: {suma_digitos(numero)}")


# 7) Un niño está construyendo una pirámide con bloques. En el nivel más bajo coloca n
# bloques, en el siguiente nivel uno menos (n - 1), y así sucesivamente hasta llegar al
# último nivel con un solo bloque.
# Escribí una función recursiva contar_bloques(n) que reciba el número de bloques en el
# nivel más bajo y devuelva el total de bloques que necesita para construir toda la
# pirámide.
    
def contar_bloques(cantidad):
    if cantidad == 1:
        return 1
    else:
        return cantidad + contar_bloques(cantidad - 1)
    
cantidad_bloques = int(input("Ingrese la cantidad de bloques del nivel más bajo para obtener la cantidad de bloques necesarios para toda la pirámide: "))
print(f"La cantidad de bloques necesarios para construir la pirámide es: {contar_bloques(cantidad_bloques)}")


#8) Escribí una función recursiva llamada contar_digito(numero, digito) que reciba un
#número entero positivo (numero) y un dígito (entre 0 y 9), y devuelva cuántas veces
#aparece ese dígito dentro del número.

def contar_digito(num, dig):
    if num <= 1:
        return 0
    else:
        # con el módulo de 10 obtengo el último dígito del número
        digito = num % 10
        #Si el digito es igual al pasado por el usuario sumo 1 al contador
        if digito == dig:
            num = num // 10  # #Dividiendo el número por 10 le quito su último dígito
            return  1 + contar_digito(num, dig)
        else:
            num = num // 10
            return  contar_digito(num, dig)
        

numero = int(input("Ingrese un número entero positivo: "))
digito = int(input("Ingrese un dígito para saber cuántas veces aparece en el número ingresado anteriormente: "))
if numero <= 0:
     print(f"{numero} no es un número entero positivo")
else:
    print(f"El dígito {digito} aparece {contar_digito(numero,digito)} veces en el número {numero}")
 