#1) Crea un programa que imprima en pantalla todos los números enteros desde 0 hasta 100
#(incluyendo ambos extremos), en orden creciente, mostrando un número por línea.
for num in range(101):
    print(num)

#2) Desarrolla un programa que solicite al usuario un número entero y determine la cantidad de
# dígitos que contiene.

numero = input("Ingrese un número para saber cuantos dígitos tiene: ")

print(f"La cantidad de dígitos que tiene {numero} es: {len(numero)}")

#3) Escribe un programa que sume todos los números enteros comprendidos entre dos valores
# dados por el usuario, excluyendo esos dos valores.

numero1 = int(input("Ingrese un número para sumar todos los enteros comprendidos entre este y el siguiente número que ingrese: "))
numero2 = int(input("Ingrese el otro número: "))
sumatoria = 0

# Con este if verifico cual de los dos números ingresados es el mayor, para poder indicar al bucle for desde que número hasta que número se repetirá.
# Si numero2 es mayo a numero1, irá de numero1 + 1 hasta numero2 y sino al revés
if numero1 < numero2:
    for num in range(numero1 + 1,numero2):
        sumatoria += num
else:
    for num in range(numero2 + 1,numero1):
        sumatoria += num

print(f"La sumatoria de todos los números enteros\ncomprendidos entre {numero1} y {numero2} es: {sumatoria}")


#4) Elabora un programa que permita al usuario ingresar números enteros y los sume en
# secuencia. El programa debe detenerse y mostrar el total acumulado cuando el usuario ingrese
# un 0.

numero = float(input("Ingrese un número para sumarlo o un 0 para finalizar el programa: "))
sumatoria = 0

while numero != 0:
    sumatoria += numero
    numero = float(input("Ingrese un número para sumarlo o un 0 para finalizar el programa: "))

print("La sumatoria de todos los números es:",sumatoria)


#5) Crea un juego en el que el usuario deba adivinar un número aleatorio entre 0 y 9. Al final, el
# programa debe mostrar cuántos intentos fueron necesarios para acertar el número.

#Importo la librería random para generar un número aleatorio entre 0 y 9
import random 
num_aleatorio = random.randint(0,9)
numero = int(input("Ingrese un número para tratar de adivinar un número entre 0 y 9: "))
intentos = 1

#Con este while valido que el usuario no ingrese números menores que 0 ni mayores que 9
while numero < 0 or numero > 9:
    print("ERROR")
    numero = int(input("Ingrese un número entre 0 y 9: "))

#Mientras el número ingresado por el usuario sea distinto al número aleatorio se sigue pidiendo que ingrese un número
while numero != num_aleatorio:
    numero = int(input("Ingrese un número para tratar de adivinar un número entre 0 y 9: "))
    #Con este while valido que el usuario no ingrese números menores que 0 ni mayores que 9
    while numero < 0 or numero > 9:
        print("ERROR")
        numero = int(input("Ingrese un número entre 0 y 9: "))
    intentos += 1

print(f"¡Bien hecho! ¡Encontrar el número solo te tomó {intentos} intentos!")


# 6) Desarrolla un programa que imprima en pantalla todos los números pares comprendidos
# entre 0 y 100, en orden decreciente.

for i in range(100 - 1 , 1 , -2):
    print(i - 1)


#7) Crea un programa que calcule la suma de todos los números comprendidos entre 0 y un
# número entero positivo indicado por el usuario.

numero = int(input("Ingrese un número para sumar todos los números comprendidos entre 0 y ese número: "))
sumatoria = 0

for num in range(1,numero):
    sumatoria += num

print("La sumatoria es:",sumatoria) 


#8) Escribe un programa que permita al usuario ingresar 100 números enteros. Luego, el
# programa debe indicar cuántos de estos números son pares, cuántos son impares, cuántos son
# negativos y cuántos son positivos. (Nota: para probar el programa puedes usar una cantidad
# menor, pero debe estar preparado para procesar 100 números con un solo cambio).

# En CANTIDAD en lugar de 9 iría un 99
CANTIDAD = 9

pares = 0
impares = 0
positivos = 0
negativos = 0

numero = int(input("Ingrese 100 números para contar cuantos son pares,\ncuantos son impares, cuantos positivos y cuantos negativos:"))

cant_num_ingresados = 1

if numero % 2 == 0:
        pares += 1
else:
        impares += 1

if numero > 0:
        positivos += 1
elif numero < 0:
        negativos += 1   

while cant_num_ingresados <= CANTIDAD:

    numero = int(input("Ingrese otro número: "))

    cant_num_ingresados += 1

    if numero % 2 == 0:
        pares += 1
    else:
        impares += 1

    if numero > 0:
        positivos += 1
    elif numero < 0:
        negativos += 1    


print(f"Pares: {pares}\nImpares: {impares}\nPositivos: {positivos}\nNegativos: {negativos}")


# 9) Elabora un programa que permita al usuario ingresar 100 números enteros y luego calcule la
# media de esos valores. (Nota: puedes probar el programa con una cantidad menor, pero debe
# poder procesar 100 números cambiando solo un valor).

# En CANTIDAD en lugar de 9 iría un 99
CANTIDAD = 9

sumatoria = 0
numero = int(input("Ingrese 100 números enteros para calcular su media: "))
cant_num_ingresados = 1
sumatoria += numero


while cant_num_ingresados <= CANTIDAD:
    numero = int(input("Ingrese otro número: "))
    cant_num_ingresados += 1
    sumatoria += numero 

print("La media de los números ingresados es: ", sumatoria / cant_num_ingresados)


# 10) Escribe un programa que invierta el orden de los dígitos de un número ingresado por el
# usuario. Ejemplo: si el usuario ingresa 547, el programa debe mostrar 745

numero = int(input("Ingrese un número para invertirlo: "))
digito = 0
inverso = 0

while numero != 0:
     
    # obtengo el último dígito del número con el módulo 10
     digito = numero % 10

    # divido el número entre 10 con doble barra para quedarme con el número entero, y así eliminar el último dígito que esté después de la coma, si es que existe alguno
     numero = numero // 10

    # Construyo el número inverso multiplicando 'inverso' por 10 y sumando el dígito actual.
     inverso = inverso * 10 + digito

print(f"El número invertido es {inverso}")