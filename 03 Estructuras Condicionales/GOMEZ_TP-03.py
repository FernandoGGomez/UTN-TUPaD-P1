#Actividades
#1) Escribir un programa que solicite la edad del usuario. Si el usuario es mayor de 18 años,
#deberá mostrar un mensaje en pantalla que diga “Es mayor de edad”

edad = int(input("Ingrese su edad: "))

if edad > 18:
    print("Es mayor de edad")

#2) Escribir un programa que solicite su nota al usuario. Si la nota es mayor o igual a 6, deberá
#mostrar por pantalla un mensaje que diga “Aprobado”; en caso contrario deberá mostrar el
#mensaje “Desaprobado”.    

nota = int(input("Ingrese su nota: "))

if nota >= 6:
    print("Aprobado")
else:
    print("Desaprobado")

#3) Escribir un programa que permita ingresar solo números pares. Si el usuario ingresa un
#número par, imprimir por pantalla el mensaje "Ha ingresado un número par"; en caso
#contrario, imprimir por pantalla "Por favor, ingrese un número par". Nota: investigar el uso del
#operador de módulo (%) en Python para evaluar si un número es par o impar.

numero = int(input("Ingrese un número par: "))

if numero % 2 == 0:
    print("Ha ingresado un número par")
else:
    print("Por favor, ingrese un número par")

#4) Escribir un programa que solicite al usuario su edad e imprima por pantalla a cuál de las
#siguientes categorías pertenece:
#● Niño/a: menor de 12 años.
#● Adolescente: mayor o igual que 12 años y menor que 18 años.
#● Adulto/a joven: mayor o igual que 18 años y menor que 30 años.
#● Adulto/a: mayor o igual que 30 años.

edad = int(input("Ingrese su edad: "))    

if edad < 12:
    print("Niño/a")
elif edad >= 12 and edad < 18:
    print("Adolescente")
elif edad >= 18 and edad < 30:
    print("Adulto/a joven")
elif edad >= 30:
    print("Adulto/a")


#5) Escribir un programa que permita introducir contraseñas de entre 8 y 14 caracteres
#(incluyendo 8 y 14). Si el usuario ingresa una contraseña de longitud adecuada, imprimir por
#pantalla el mensaje "Ha ingresado una contraseña correcta"; en caso contrario, imprimir por
#pantalla "Por favor, ingrese una contraseña de entre 8 y 14 caracteres". Nota: investigue el uso
#de la función len() en Python para evaluar la cantidad de elementos que tiene un iterable tal
#como una lista o un string.

contraseña = input("Ingrese una contraseña de entre 8 y 14 caracteres: ")

if len(contraseña) >= 8 and len(contraseña) <= 14:
    print("Ha ingresado una contraseña correcta")
else:
    print("Por favor, ingrese una contraseña de entre 8 y 14 caracteres")

#6) El paquete statistics de python contiene funciones que permiten tomar una lista de números
#y calcular la moda, la mediana y la media de dichos números. Un ejemplo de su uso es el
#siguiente:
#from statistics import mode, median, mean
#mi_lista = [1,2,5,5,3]
#mean(mi_lista)
#En la documentación oficial se puede encontrar más información sobre este paquete:
#https://docs.python.org/es/3.8/library/statistics.html.
#La moda (mode), la mediana (median) y la media (mean) son parámetros estadísticos que se
#pueden utilizar para predecir la forma de una distribución normal a partir del siguiente criterio:
#● Sesgo positivo o a la derecha: cuando la media es mayor que la mediana y, a su vez, la
#mediana es mayor que la moda.
#● Sesgo negativo o a la izquierda: cuando la media es menor que la mediana y, a su vez,
#la mediana es menor que la moda.
#● Sin sesgo: cuando la media, la mediana y la moda son iguales.
#Teniendo en cuenta lo antes mencionado, escribir un programa que tome la lista
#numeros_aleatorios, calcule su moda, su mediana y su media y las compare para determinar si
#hay sesgo positivo, negativo o no hay sesgo. Imprimir el resultado por pantalla.
#Definir la lista numeros_aleatorios de la siguiente forma:
#import random
#numeros_aleatorios = [random.randint(1, 100) for i in range(50)]
#Nota: el bloque de código anterior crea una lista con 50 números entre 1 y 100 elegidos de
#forma aleatoria.

from statistics import mode, median, mean
import random

numeros_aleatorios = [random.randint(1,100) for i in range(50)]
moda = mode(numeros_aleatorios)
mediana = median(numeros_aleatorios)
media = mean(numeros_aleatorios)

print("moda:",moda)
print("mediana:",mediana)
print("media:",media)

if media > mediana and mediana > moda:
    print("Sesgo positivo")
elif media < mediana and mediana < moda:
    print("Sesgo Negativo")
elif media == mediana and media == moda:
    print("Sin sesgo")
else:
    pass

#7) Escribir un programa que solicite una frase o palabra al usuario. Si el string ingresado
#termina con vocal, añadir un signo de exclamación al final e imprimir el string resultante por
#pantalla; en caso contrario, dejar el string tal cual lo ingresó el usuario e imprimirlo por
#pantalla.

frase = input("Ingrese una frase o palabra: ")
#Para saber la posición de la última letra debo restarle 1, porque el método len() comienza contando desde la posición 0
ultima_letra = frase[len(frase) - 1]

if ultima_letra == "a" or ultima_letra == "A": 
    print(frase + "!")    
elif ultima_letra == "e" or ultima_letra == "E":
    print(frase + "!")
elif ultima_letra == "i" or ultima_letra == "I":
    print(frase + "!")
elif ultima_letra == "o" or ultima_letra == "O":
    print(frase + "!")
elif ultima_letra == "u" or ultima_letra == "U":
    print(frase + "!")
else:
    print(frase)


#8) Escribir un programa que solicite al usuario que ingrese su nombre y el número 1, 2 o 3
#dependiendo de la opción que desee:
#1. Si quiere su nombre en mayúsculas. Por ejemplo: PEDRO.
#2. Si quiere su nombre en minúsculas. Por ejemplo: pedro.
#3. Si quiere su nombre con la primera letra mayúscula. Por ejemplo: Pedro.
#El programa debe transformar el nombre ingresado de acuerdo a la opción seleccionada por el
#usuario e imprimir el resultado por pantalla. Nota: investigue uso de las funciones upper(),
#lower() y title() de Python para convertir entre mayúsculas y minúsculas.

nombre = input("Ingrese su nombre: ")
opcion = int(input(f"Presione 1 si quiere su nombre en mayúsculas \nPresione 2 si quiere su nombre en minúsculas \nPresione 3 si quiere su nombre con la primera letra mayúscula \n "))

if opcion == 1:
    print(nombre.upper())
elif opcion == 2:
    print(nombre.lower())
elif opcion == 3:
    print(nombre.title())    

#9) Escribir un programa que pida al usuario la magnitud de un terremoto, clasifique la
#magnitud en una de las siguientes categorías según la escala de Richter e imprima el resultado
#por pantalla:
#● Menor que 3: "Muy leve" (imperceptible).
#● Mayor o igual que 3 y menor que 4: "Leve" (ligeramente perceptible).
#● Mayor o igual que 4 y menor que 5: "Moderado" (sentido por personas, pero
#generalmente no causa daños).
#● Mayor o igual que 5 y menor que 6: "Fuerte" (puede causar daños en estructuras
#débiles).
#● Mayor o igual que 6 y menor que 7: "Muy Fuerte" (puede causar daños significativos).
#● Mayor o igual que 7: "Extremo" (puede causar graves daños a gran escala).

magn_terremoto = float(input("Ingrese la magnitud de un terremoto: "))

if magn_terremoto < 3:
    print('"Muy leve" (imperceptible).')
elif magn_terremoto >= 3 and magn_terremoto < 4:
    print('"Leve" (Ligeramente perceptible).')
elif magn_terremoto >= 4 and magn_terremoto < 5:
    print('"Moderado" (sentido por personas, pero generalmente no causa daños).')
elif magn_terremoto >= 5 and magn_terremoto < 6:
    print('"Fuerte" (puede causar daños significativos).')
elif magn_terremoto >= 6 and magn_terremoto < 7:
    print('"Muy Fuerte" (puede causar daños significativos).')
elif magn_terremoto >= 7:
    print('"Extremo" (puede causar graves daños a gran escala).')


#10) Utilizando la información aportada en la siguiente tabla sobre las estaciones del año
#Periodo del año                         Estación en el                  Estación en el 
#                                        hemisferio norte                hemisferio sur
#                       
#Desde el 21 de diciembre hasta              Invierno                        Verano
# el 20 de
#marzo (incluidos)         



#Desde el 21 de marzo hasta                  Primavera                        Otoño
# el 20 de junio
#(incluidos)       


                            
#Desde el 21 de junio hasta el 20 de
#septiembre (incluidos)                          Verano                       Invierno

#Desde el 21 de septiembre hasta el 20 de
#diciembre (incluidos)                           Otoño                          Primavera


#Escribir un programa que pregunte al usuario en cuál hemisferio se encuentra (N/S), qué mes
#del año es y qué día es. El programa deberá utilizar esa información para imprimir por pantalla
#si el usuario se encuentra en otoño, invierno, primavera o verano.

hemisferio = input("En que hemisferio se encuentra (N/S): ").lower()
mes = int(input("Que mes del año es en número: "))
dia = int(input("Que dia es en número: "))

if hemisferio == "n" :
    if (dia >= 21 and mes == 12) or mes == 1 or mes == 2 or (dia < 21 and mes == 3):
        print("Invierno")
    elif (dia >= 21 and mes == 3) or mes == 4 or mes == 5 or (dia < 21 and mes == 6):
        print("Primavera")
    elif (dia >= 21 and mes == 6) or mes == 7 or mes == 8 or (dia < 21 and mes == 9):
        print("Vernao")
    elif (dia >= 9 and mes == 10) or mes == 11 or mes == 12 or (dia < 21 and mes == 12):
        print("Otoño")
elif hemisferio == "s":
        if (dia >= 21 and mes == 12) or mes == 1 or mes == 2 or (dia < 21 and mes == 3):
            print("Verano")
        elif (dia >= 21 and mes == 3) or mes == 4 or mes == 5 or (dia < 21 and mes == 6):
            print("Otoño")
        elif (dia >= 21 and mes == 6) or mes == 7 or mes == 8 or (dia < 21 and mes == 9):
            print("invierno")
        elif (dia >= 9 and mes == 10) or mes == 11 or mes == 12 or (dia < 21 and mes == 12):
            print("Primavera")