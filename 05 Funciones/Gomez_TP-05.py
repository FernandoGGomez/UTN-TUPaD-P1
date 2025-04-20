#1. Crear una función llamada imprimir_hola_mundo que imprima por
#pantalla el mensaje: “Hola Mundo!”. Llamar a esta función desde el
#programa principal.

def imprimir_hola_mundo():
    print("Hola Mundo!")


#2. Crear una función llamada saludar_usuario(nombre) que reciba
#como parámetro un nombre y devuelva un saludo personalizado.
#Por ejemplo, si se llama con saludar_usuario("Marcos"), deberá de-
#volver: “Hola Marcos!”. Llamar a esta función desde el programa
#principal solicitando el nombre al usuario.

def saludar_usuario(nombre):
    print(f"Hola {nombre}!")


#3. Crear una función llamada informacion_personal(nombre, apellido,
#edad, residencia) que reciba cuatro parámetros e imprima: “Soy
#[nombre] [apellido], tengo [edad] años y vivo en [residencia]”. Pe-
#dir los datos al usuario y llamar a esta función con los valores in-
#gresados.

def informacion_personal(nombre, apellido, edad, residencia):
    print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}")


def leer_entero_validado(mensaje, min = float("-Inf"), max = float("Inf")):
    num = int(input(f"{mensaje} "))
    while num < min or num > max:
        num = int(input(f"ERROR. {mensaje} "))
    return num

#4. Crear dos funciones: calcular_area_circulo(radio) que reciba el ra-
#dio como parámetro y devuelva el área del círculo. calcular_peri-
#metro_circulo(radio) que reciba el radio como parámetro y devuel-
#va el perímetro del círculo. Solicitar el radio al usuario y llamar am-
#bas funciones para mostrar los resultados.
from  math import pi , trunc

def calcular_area_circulo(radio):
    print(f"Área: {pi * (radio ** 2)}") 

def calcular_perimetro_circulo(radio):
    print(f"Perímetro: {2 * pi * radio}")


#5. Crear una función llamada segundos_a_horas(segundos) que reciba
#una cantidad de segundos como parámetro y devuelva la cantidad
#de horas correspondientes. Solicitar al usuario los segundos y mos-
#trar el resultado usando esta función.

def segundos_a_horas(segundos):
    print(f"Horas: {segundos / 60 / 60}")



#6. Crear una función llamada tabla_multiplicar(numero) que reciba un
# número como parámetro y imprima la tabla de multiplicar de ese
# número del 1 al 10. Pedir al usuario el número y llamar a la fun-
# ción.

def tabla_multiplicar(numero):
    for i in range(1,11):
        print(f"{numero}x{i} = {numero * i}")


#7. Crear una función llamada operaciones_basicas(a, b) que reciba
# dos números como parámetros y devuelva una tupla con el resulta-
# do de sumarlos, restarlos, multiplicarlos y dividirlos. Mostrar los re-
# sultados de forma clara.

def operaciones_basicas(a, b):
    suma = a + b
    resta = a - b
    multiplicacion = a * b
    division = a / b

    return (suma,resta,multiplicacion,division)



#8. Crear una función llamada calcular_imc(peso, altura) que reciba el
# peso en kilogramos y la altura en metros, y devuelva el índice de
# masa corporal (IMC). Solicitar al usuario los datos y llamar a la fun-
# ción para mostrar el resultado con dos decimales.
def calcular_imc(peso, altura):
    imc = peso /(altura ** 2)
    print(f"Imc: {truncar_imc(imc)}")

def truncar_imc(imc):
    return trunc(imc * 100) / 100

def leer_decimal_validado(mensaje, min = float("-Inf"), max = float("Inf")):
    num = float(input(f"{mensaje} "))
    while num < min or num > max:
        num = float(input(f"ERROR. {mensaje} "))
    return num

#9. Crear una función llamada celsius_a_fahrenheit(celsius) que reciba
# una temperatura en grados Celsius y devuelva su equivalente en
# Fahrenheit. Pedir al usuario la temperatura en Celsius y mostrar el
# resultado usando la función.
def celsius_a_fahrenheit(celsius):
    fahrenheit = ((9/5) * celsius) + 32
    print(f"Grados Fahrenheit: {fahrenheit}")


#10.Crear una función llamada calcular_promedio(a, b, c) que reciba
# tres números como parámetros y devuelva el promedio de ellos.
# Solicitar los números al usuario y mostrar el resultado usando esta función

def calcular_promedio(a, b, c):
    return (a + b + c) / 3

#Programa principal
#1 
imprimir_hola_mundo()

#2
nombre = input("Ingrese su nombre: ")
saludar_usuario(nombre)

#3
nombre = input("Ingrese su nombre: ")
apellido = input("Ingrese su apellido: ")
edad = leer_entero_validado("Ingrese su edad:",1)
residencia = input("Ingrese su residencia: ")

informacion_personal(nombre, apellido, edad, residencia)

#4
radio = leer_entero_validado("Ingrese el radio de un círculo:",1)
calcular_area_circulo(radio)
calcular_perimetro_circulo(radio)

#5
segundos = leer_entero_validado("Ingrese una cantidad de segundos:")
segundos_a_horas(segundos)

#6
numero = leer_entero_validado("Ingrese un número para saber su tabla de multiplicar:",1)
tabla_multiplicar(numero)

#7
num1 = leer_entero_validado("Ingrese un número hacer operaciones básicas con otro número:")
num2 = leer_entero_validado("Ingrese el otro número:")
resultados = operaciones_basicas(num1,num2)

print(f"Suma: {num1} + {num2} = {resultados[0]}")
print(f"Resta: {num1} - {num2} = {resultados[1]}")
print(f"Multiplicación: {num1} * {num2} = {resultados[2]}")
print(f"División: {num1} / {num2} = {resultados[3]}")

#8
peso = leer_decimal_validado("Ingrese un peso en Kg:",1)
altura = leer_decimal_validado("Ingrese una estatura en m:")

calcular_imc(peso,altura)

#9
celsius = leer_decimal_validado("Ingrese una temperatura en grados Celcius:")
celsius_a_fahrenheit(celsius)

#10
a = leer_entero_validado("Ingrese el primero de 3 números para sacar un promedio:")
b = leer_entero_validado("Ingrese el segundo número:")
c = leer_entero_validado("Ingrese el tercer número:")

promedio = calcular_promedio(a, b, c)

print(f"Promedio: {promedio}")

