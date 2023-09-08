# 1. Haz un programa que lea 2 números e imprima True si el primero es 20 veces el valor del segundo. Si no, imprime False.
a = int(input())
b = int(input())
if a >= (b * 20):
    print(True)
else:
    print(False)

# 2. Haz un programa que lea tres números e imprima el producto de los tres dividido entre la suma de los tres.
a = int(input())
b = int(input())
c = int(input())
print((a * b * c) / (a + b + c))

# 3. Haz un programa que lea 3 números e imprima True si están en orden ascendiente. Si no, imprime False.
a = int(input())
b = int(input())
c = int(input())
if a < b and a < c and b < c:
    print(True)
else: 
    print(False)

# 4. Haz un programa lea 4 números e imprima True si todos son negativos. Si alguno es positivo, imprime False.
a = int(input())
b = int(input())
c = int(input())
d = int(input())
if a < 0.0 and b < 0.0 and c < 0.0 and d < 0.0:
    print(True)
else: 
    print(False)

# 5. Haz un programa que lea un número e imprima True si es un número par e imprima False si es un número impar.
a = int(input())

if (a % 2) == 0:
    print(True)
else: 
    print(False)

# 6. Haz un programa que lea 3 números e imprima True si el primero es menor que el segundo y si el segundo no es igual al tercero. Si no, imprime false.
a = int(input())
b = int(input())
c = int(input())

if a < b and b != c:
    print(True)
else: 
    print(False)

# 7. Haz un programa que lea 3 números e imprima True si el primero y el segundo son iguales o si el primero es al menos 3 unidades más grande que el segundo. Si no, imprime False.
a = int(input())
b = int(input())
c = int(input())

if a == b or a >= (b + 3):
    print(True)
else: 
    print(False)

# 8. Haz un programa que lea 8 números e imprima el promedio.
a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())
f = int(input())
g = int(input())
h = int(input())

print((a + b + c + d + e + f + g + h) / 8)


# 9. Haz un programa que lea 4 strings y los concatene.
nombre = input()
edad = int(input())
ciudad = input()
actividad = input()

print("Hola mi nombre es",nombre,", tengo",edad, "años. Vivo en",ciudad, "y una de mis actividades favoritas es",actividad)