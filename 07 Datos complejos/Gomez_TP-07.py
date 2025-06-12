# Actividades
# 1) Dado el diccionario precios_frutas
# precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva':
# 1450}
# Añadir las siguientes frutas con sus respectivos precios:
# ● Naranja = 1200
# ● Manzana = 1500
# ● Pera = 2300

precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva': 1450}

precios_frutas['Naranja'] = 1200
precios_frutas['Manzana'] = 1500
precios_frutas['Pera'] = 2300

print(f"1) Precios de frutas: {precios_frutas}")
 
# 2) Siguiendo con el diccionario precios_frutas que resulta luego de ejecutar el código
# desarrollado en el punto anterior, actualizar los precios de las siguientes frutas:
# ● Banana = 1330
# ● Manzana = 1700
# ● Melón = 2800

precios_frutas['Banana'] = 1330
precios_frutas['Manzana'] = 1700
precios_frutas['Melón'] = 2800

print(f"2) Precios de frutas: {precios_frutas}")


# 3) Siguiendo con el diccionario precios_frutas que resulta luego de ejecutar el código
# desarrollado en el punto anterior, crear una lista que contenga únicamente las frutas sin los
# precios.

frutas = [precios_frutas.keys()]

print(f"3) Frutas: {frutas}")


# 4) Escribí un programa que permita almacenar y consultar números telefónicos.
# • Permití al usuario cargar 5 contactos con su nombre como clave y número como valor.
# • Luego, pedí un nombre y mostrale el número asociado, si existe.
# Ejemplo:
    #contactos = {"Juan": "123456", "Ana": "987654"}
    #Consultar: "Juan" → muestra "123456"

print("4) Agende 5 contactos")
cont = 1
contactos = {}
while cont <= 5:
    
    nombre = input("Ingrese un nombre: ").lower().capitalize()

    numero = input("Ingrese un número de teléfono: ")

    contactos[nombre] = numero 
    cont += 1


consulta = input("Escriba un nombre de la lista para obtener su número de teléfono: ").lower().capitalize()

print(f"Número de teléfono de {consulta}: {contactos[consulta]}")

print(f"Agenda: {contactos}")



# 5) Solicita al usuario una frase e imprime:
# • Las palabras únicas (usando un set).
# • Un diccionario con la cantidad de veces que aparece cada palabra.

frase = input("5) Ingrese una frase con palabras repetidas: ").split() #Convierto la frase ingresada en una lista de elementos separados por un espacio
palabras_unicas = set() #Inicializo un set vacío
recuento = {} #Inicializo un diccionario vacío

for i in range(0, len(frase)):
    palabras_unicas.add(frase[i]) #Añado cada uno de los elementos al set
    if frase[i] in recuento:  #Si la clave ya se encuentra en el diccionario, le sumo 1
        recuento[frase[i]] += 1
    else:
        recuento[frase[i]] = 1  #Si no, lo agrego con un valor de 1

print(f"Palabras únicas: {palabras_unicas}")
print(f"Recuento: {recuento} ")


# 6) Permití ingresar los nombres de 3 alumnos, y para cada uno una tupla de 3 notas.
# Luego, mostrá el promedio de cada alumno.

print("6) Ingrese el nombre y las notas de 3 alumnos")
cont = 1
alumnos = {}

while cont <= 3:
    
    nombre = input("Ingrese el nombre del primer alumno/a: ").lower().capitalize()
    nota1 = int(input("Ingrese la primer nota: "))
    nota2 = int(input("Ingrese la segunda nota: "))
    nota3 = int(input("Ingrese la tercer nota: "))

    alumnos[nombre] = (nota1, nota2, nota3)
    
    cont += 1

nombres = list(alumnos.keys()) #Guardo los nombres en una lista
for nombre in range(0, len(alumnos)):  #Recorro todos los alumnos guardados en el diccionario
    suma = 0
    for nota in alumnos[nombres[nombre]]: #Por cada usuario accedo a sus notas y las sumo
           suma += nota 
    print(f"Promedio notas de {nombres[nombre]}: {suma / 3}") #Imprimo el promedio de las notas una vez por usuario/ciclo del for principal



# 7) Dado dos sets de números, representando dos listas de estudiantes que aprobaron Parcial 1
# y Parcial 2:
# • Mostrá los que aprobaron ambos parciales.
# • Mostrá los que aprobaron solo uno de los dos.
# • Mostrá la lista total de estudiantes que aprobaron al menos un parcial (sin repetir).


aprobaron_parcial_1 = {1,2,3,4}
aprobaron_parcial_2 = {1,5,6,3}

ambos_aprobados = aprobaron_parcial_1.intersection(aprobaron_parcial_2)
solo_uno_aprobado = aprobaron_parcial_1.symmetric_difference(aprobaron_parcial_2)
al_menos_uno_aprobado = aprobaron_parcial_1.union(aprobaron_parcial_2)

print("7)", end=" ")

print(f"Los que aprobaron ambos parciales: {ambos_aprobados}")
print(f"Los que aprobaron solo un parcial: {solo_uno_aprobado}")
print(f"Los que aprobaron al menos un parcial: {al_menos_uno_aprobado}")


# 8) Armá un diccionario donde las claves sean nombres de productos y los valores su stock.
# Permití al usuario:
# • Consultar el stock de un producto ingresado.
# • Agregar unidades al stock si el producto ya existe.
# • Agregar un nuevo producto si no existe.

diccionario_productos = {'Procesador': 1200, 'Tarjeta Gráfica': 2500, 'Monitor': 3000, 'Mouse': 1450}
print("8)")
activo = True
while activo:
    productos = list(diccionario_productos.keys())
    print("Lista de productos: ",productos)
    for producto in range(0,len(productos)):
        print(f"Ingrese el número {producto + 1} para consultar el stock del producto {productos[producto]}")

    print(f"Si quiere agregar un producto que no se encuentra en la lista presione la tecla A")
    print("Escriba -1 para terminar")

    opcion = input() 
    if opcion.isdigit():
        opcion = int(opcion)
            
        print(f"Stock {productos[opcion-1]}: {diccionario_productos[productos[opcion-1]]}")
        print("Si quiere agregar sumar unidades al stock presione 1: ")
        print("Si quiere volver atrás presione 2: ")
        opcion = int(input())
        if opcion == 1:
            unidades = int(input("Ingrese la cantidad de unidades que desea agregar al stock: "))
            diccionario_productos[productos[opcion-1]] += unidades
            print(f"Stock {productos[opcion-1]}: {diccionario_productos[productos[opcion-1]]}")

    elif opcion == "-1":
            activo = False
    
    else:
        opcion.lower()
        if opcion == "a":
            nombre = input("Ingrese el nombre del producto: ").capitalize()
            stock = int(input("Ingrese el stock del producto: "))

            diccionario_productos[nombre] = stock

#9) Creá una agenda donde las claves sean tuplas de (día, hora) y los valores sean eventos.
#Permití consultar qué actividad hay en cierto día y hora.
agenda = {  ("Lunes","12:00"):"Estudiar Matemática",
            ("Martes","16:00"):"Estudiar Programación", 
            ("Martes","19:00"):"Hacer las compras ", 
            ("Miércoles","12:00"):"Estudiar AySO",
            ("Jueves","16:00"):"Entregar TPI OE", 
            ("Viernes","12:00"):"Entregar TPI Matemática",
            ("Sábado","20:00"):"Segundo Parcial Programación 1"}

dias_agenda = list(agenda.keys())

print(f"9) Agenda: {agenda}")

activo = True

while activo:
    opcion = input("Ingrese un día de la semana para revisar que hay en la agenda o -1 para salir: ")

    if opcion == "-1":
        activo = False
    else:
        opcion.lower()
        for dia in dias_agenda:
            if opcion == dia[0].lower():
                print(f"{dia[0]} {dia[1]}hs: {agenda[dia]}")
               

# Dado un diccionario que mapea nombres de países con sus capitales, construí un nuevo
# diccionario donde:
# • Las capitales sean las claves.
# • Los países sean los valores.

original = {"Argentina": "Buenos Aires","Chile": "Santiago", "Brasil": "Brasilia", "Paraguay": "Asunción", "Perú": "Lima" }

print(f"10) Diccionario original {original}")

claves = list(original.keys())
valores = list(original.values())
invertido = {}
for i in range(0,len(original)):
    invertido[valores[i]] = claves[i]

print(f"Invertido: {invertido}")