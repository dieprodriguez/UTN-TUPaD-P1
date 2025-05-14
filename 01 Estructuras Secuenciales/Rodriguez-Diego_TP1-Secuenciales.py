import math
#1) Crear un programa que imprima por pantalla el mensaje: “Hola Mundo!”.
print("HOla Mundo")

#2) Crear un programa que pida al usuario su nombre e imprima por pantalla un saludo usandoel nombre ingresado. Por ejemplo: si el usuario ingresa “Marcos”, el programa debe imprimir por pantalla “Hola Marcos!”. Consejo: esto será más sencillo si utilizas print(f…) para realizar la impresión por pantalla.
nombre = input("Ingrese su nombre: ")
print(f"Hola {nombre}!")

#3) Crear un programa que pida al usuario su nombre, apellido, edad y lugar de residencia e imprima por pantalla una oración con los datos ingresados. Por ejemplo: si el usuario ingresa “Marcos”, “Pérez”, “30” y “Argentina”, el programa debe imprimir “Soy Marcos Pérez, tengo 30 años y vivo en Argentina”. Consejo: esto será más sencillo si utilizas print(f…) para realizar la impresión por pantalla.
nombre =input("Ingrese su nombre: ")
apellido =input("Ingrese su apellido: ")
edad =input("Ingrese su edad: ")
ciudad =input("Ingrese su lugar de residencia: ")
print (f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {ciudad}")

#4) Crear un programa que pida al usuario el radio de un círculo e imprima por pantalla su área y su perímetro. 
radio = float(input("Ingrese el valor del radio del círculo que desea calcular: "))
area = math.pi*radio**2
perimetro = 2*math.pi*radio
print(f"El área del círculo de radio {radio} es {area} y su perímetro es {perimetro}")

#5) Crear un programa que pida al usuario una cantidad de segundos e imprima por pantalla a cuántas horas equivale. 
seg = int(input("Igrese la cantidad de segundos: "))
hora = seg/3600
print(f"{seg} segundos equivalen a {hora} horas")

#6) Crear un programa que pida al usuario un número e imprima por pantalla la tabla de multiplicar de dicho número. 
numero = int(input("Ingrese un número: "))
print(f"{numero}x1 = ",numero*1)
print(f"{numero}x2 = ",numero*2)
print(f"{numero}x3 = ",numero*3)
print(f"{numero}x4 = ",numero*4)
print(f"{numero}x5 = ",numero*5)
print(f"{numero}x6 = ",numero*6)
print(f"{numero}x7 = ",numero*7)
print(f"{numero}x8 = ",numero*8)
print(f"{numero}x9 = ",numero*9)
print(f"{numero}x10 = ",numero*10)

#7) Crear un programa que pida al usuario dos números enteros distintos del 0 y muestre por pantalla el resultado de sumarlos, dividirlos, multiplicarlos y restarlos.
num1 = int(input ("Ingrese un número entero distinto de cero: "))
num2 = int(input ("Ingrese otro número entero distinto de cero: "))
suma = num1 + num2
division = num1 / num2
multiplicacion = num1 * num2 
resta =num1 - num2
print (f"La suma entre {num1} y {num2} es: {suma}")
print (f"La división entre {num1} y {num2} es: {division}")
print (f"La multiplicación entre {num1} y {num2} es: {multiplicacion}")
print (f"La resta entre {num1} y {num2} es: {resta}")

#8) Crear un programa que pida al usuario su altura y su peso e imprima por pantalla su índice de masa corporal.
peso = float(input ("Ingrese su peso en kg: "))
altura = float(input ("Ingrese su altura en metros: "))
imc = peso/(altura**2)
print(f"Su indice de masa corporal IMC es: {imc}")

#9) Crear un programa que pida al usuario una temperatura en grados Celsius e imprima por pantalla su equivalente en grados Fahrenheit.
temp_celsius = float(input ("Ingrese la temperatura en °C: "))
temp_farenheit = (temp_celsius * 9/5) + 32
print(f"{temp_celsius} °C son equivalentes a: {temp_farenheit} °F")

# 10) Crear un programa que pida al usuario  3 números e imprima por pantalla el promedio de dichos números.
num1 = float(input ("Ingrese un número: "))
num2 = float(input ("Ingrese otro número: "))
num3 = float(input ("Ingrese otro número: "))
promedio_num = (num1 + num2 + num3)/3
print(f"El promedio entre {num1}, {num2} y {num3} es: {promedio_num}")
