# 1. Escribe un programa que le pida al usuario que introduzca un mes (ej. enero, febrero, etc.). El programa debe imprimir cuantos días hay en ese mes (asume un año no bisiesto).

mes = input("Escribe un mes: ")
if mes == "Enero" or mes == "enero":
    print("Enero tiene 31 días")
elif mes == "Febrero" or mes == "febrero":
    print("Febrero tiene 28 días")
elif mes == "Marzo" or mes == "marzo":
    print("Marzo tiene 31 días")
elif mes == "Abril" or mes == "abril":
    print("Abril tiene 30 días")
elif mes == "Mayo" or mes == "mayo":
    print("Mayo tiene 31 días")
elif mes == "Junio" or mes == "junio":
    print("Junio tiene 30 días")
elif mes == "Julio" or mes == "julio":
    print("Julio tiene 31 días")
elif mes == "Agosto" or mes == "agosto":
    print("Agosto tiene 31 días")
elif mes == "Septiembre" or mes == "septiembre":
    print("Septiembre tiene 30 días")
elif mes == "Octubre" or mes == "octubre":
    print("Octubre tiene 31 días")
elif mes == "Noviembre" or mes == "noviembre":
    print("Noviembre tiene 30 días")
elif mes == "Diciembre" or mes == "Diciembre":
    print("Diciembre tiene 31 días")
else:
    print(input("Porfavor escribe un mes:"))

# 2. Escribe un programa que le pida al usuario que introduzca un día de la semana (ej. lunes, martes, etc.). El programa debe imprimir la posición de ese día en la semana. En este ejemplo asumimos que la semana empieza en lunes por lo que lunes sería 1, martes sería 2, etc.
dia = input("Escribe un dia: ")
if dia == "Lunes" or dia == "lunes":
    print("Lunes es el dia 1 de la semana")
elif dia == "Martes" or dia == "martes":
    print("Martes es el dia 2 de la semana")
elif dia == "Miercoles" or dia == "miercoles":
    print("Miercoles es el dia 3 de la semana")
elif dia == "Jueves" or dia == "jueves":
    print("Jueves es el dia 4 de la semana")
elif dia == "Viernes" or dia == "viernes":
    print("Viernes es el dia 5 de la semana")
elif dia == "Sabado" or dia == "sabado":
    print("Sabado es el dia 6 de la semana")
elif dia == "Domingo" or dia == "domingo":
    print("Domingo es el dia 7 de la semana")
else:
    print(input("Escribe un dia de la semana: "))

# 3. 
año = int(input("Escribe un año: "))
if año % 400 == 0:
    print("Bisiesto")
elif año % 4 == 0 and año % 100 != 0:
    print("Es año biesto")
else:
    print("No bisiesto")

#4. 
numero = int(input("Escribe un numero: "))
if numero > 0:
    a = "Es un numero positivo."
else:
    a = "Es un numero negativo."

if numero % 2 == 0:
    b= "Es un numero par."
else:
    b = "Es un numero impar."

if numero > 100:
    c = "Es un numero mayor que 100."
else:
    c = "Es un numero menor que 100."

print(a,b,c)

# 6. Imprime lo siguiente: Si Si Do Re Re Do Si La Sol Sol La Si Si La La (accediendo al arreglo, no es válido directamente imprimir tales palabras).
notas = ["Do", "Re", "Mi", "Fa", "Sol", "La", "Si"]
notas.pop()
notas.insert(0, "Si")
notas.insert(0, "Si")
notas.insert(4, "Re")
notas.insert(5, "Do")
notas.insert(6, "Si")
notas.insert(7, "La")
notas.pop(8)
notas.pop(8)
notas.insert(8, "Sol")
notas.append("Si")
notas.append("Si")
notas.append("La")
notas.append("La")

print(notas)

# 7. Dado el siguiente arreglo = [ “Jose Miguel”, “Carlos”, “Manuel”, “Memo” ], reciba unstring del usuario e indique si ese string aparece dentro del arreglo o no, puedes regresar “True” si el elemento está dentro del arreglo o “False” si el elemento no está dentro del arreglo
nombres = ["Jose Miguel", "Carlos", "Manuel", "Memo"]
tunombre = input("Escribe tu nombre: ")
if tunombre == nombres[0] or tunombre == nombres[1] or tunombre == nombres[2] or tunombre == nombres[3]:
    print(True)
else:
    print(False)


# 8. Dado el siguiente arreglo = [12,456,2,123], ordenalo e imprimelo siendo [2,12,123,456].
numeros = [12,456,2,123]
numeros.sort()
print(numeros)


# 9. 
lista =[]
pares = 0
impares = 0

for i in range(0,6):
    lista.append(int(input()))

for i in range(0,6):
    if i%2 == 0:
        pares += lista[i]
        
    else:
        impares += lista[i]
        
print()
print("Resultado = ", pares - impares)


# 10. Palindromo o no palindromo
lista = []
for i in range(0,6):
    lista.append(int(input()))

if lista[0] == lista[4] and lista[1] == lista[3]:
    print("Es palindromo")
else:
    print("No es palindromo")

# 11. 
from math import sqrt
lado = float(input())
diagonal = float(input())
lado2 = (round(sqrt((diagonal * diagonal) - (lado * lado))))
if lado2 == lado:
    print("Esto es un cuadrado")
else:
    print("Esto es un rectángulo")