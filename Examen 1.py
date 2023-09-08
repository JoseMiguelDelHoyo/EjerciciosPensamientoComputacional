#1. 
Corriente = int(input("Escribe el valor de la corriente eléctrica: "))
Resistencia = int(input("Escribe el valor de la resistencia: " ))
Voltaje = Corriente * Resistencia
print(Voltaje)


#2. 
pasado = int(input("Escribe el precio de los vuelos del año pasado: "))
presente = 8000
diferencia = presente - pasado
incremento = ((presente / pasado) * 100) - 100
print("La diferencia de precio es", diferencia, ". El incremento en el precio fue de ", incremento, "%.")

#3. 
a = int(input("Escribe un numero: "))
if a % 2 == 0:
    print("Par")
else:
    print("Impar")

#4. 
libros = ["Biblia", "Corán", "Principito", "El diario de Greg", "Programación en Python", "Algoritmos Avanzados", "Algebra de Baldor"]
libros.pop()
libros.pop()
libros.append("Harry Potter")
libros.append("Cambios atómicos")
libros.pop(0)
libros.insert(5, "Biblia")
libros.pop(1)
libros.insert(0, "Principito")

print(libros)

#5. 
pen = int(input("Escribe el valor del lado del pentagono: "))
apen = int(input("Escribe el valor del apotema del pentagono: "))
hex = int(input("Escribe el valor del lado del hexagono: "))
ahex = int(input("Escribe el valor del apotema del hexagono: "))
peripen = (pen * 5)
perihex = (hex * 6)
areapen = ((peripen * apen) / 2)
areahex = ((perihex * ahex) / 2)
if areapen > areahex:
    print("Usa llantas pentagonales")
else:
    print("Usa llantas hexagonales")



#6 .append - .insert - .pop

#7. .len

#8. Un string es una palabra que almacena un dato, ya sea un numero o una palabra. Ej. a = "Hola Mundo"

#9. Un tipo de dato es el booleano, este se refiere a que solo puede ser verdadero o falso. Otro tipo de dato son los numeros, los cuales se clasifican en numeros enteros o numeros con punto decimal. Otro tipo de dato son los strings, los cuales son listas, es decir, tiene muchos datos.

#10. Una variable es lo contrario a una constante. Una variable es un dato que se puede alterar o cambiar.

#11. And se refiere a que se tienen que cumplir dos condiciones, o más, para que el código funciones. Or se refiere a que solo tiene que funcionar una de las funciones para que funcione el código. Not se refiere a que ninguna de las condiciones debe funcionar para que funcione el código.

#12
from math import sqrt
lado = int(input("Escribe el valor del lado del triángulo: "))
altura = (sqrt((lado * lado) - ((lado / 2) * (lado / 2))))
area = ((lado * altura) / 2)
print(area)

#13
a = input("Escribe un texto: ")
if len(a) > 500:
    print("Error")

