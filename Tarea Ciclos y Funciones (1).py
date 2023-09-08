#!/usr/bin/env python
# coding: utf-8

# # Problema 1

# In[3]:


a = int(input())
b = 0
for i in range(1,a+1):
    b += i
    print(b)


# ## Problema 2

# In[24]:


a = 1
x = 0
lista = []
while a != 0:
    a = int(input())
    lista.append(a)

for i in lista:
    x += i
print(x/len(lista))


# # Problema 3

# In[8]:


listaCompras = []
n = int(input("Cuátos elementos quieres en tu lista: "))
for i in range(0,n):
    elemento = input()
    listaCompras.append(elemento)
    listaCompras.sort()
print(listaCompras)


# # Problema 4

# In[18]:


listaNum = []
n = int(input("Cuántos numeros quieres en tu lista: "))
for i in range(n):
    numeros = int(input())
    if numeros % 2 == 0:
        listaNum.append(numeros)
print(listaNum)


# # Problema 5

# In[19]:


x = "Hola mi nombre es José Miguel"

for i in x:
    if i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u':
        print(i)
    else:
        None


# # Problema 6

# In[26]:


def booleano():
    numero = int(input('dame un numero: '))
    if numero%243 == 0:
        return True
    else:
        return False

    
booleano()


# # Problema 7

# In[28]:


def multiplicarString():
    string = input()
    numero = int(input())
    print(string * numero)
    return
multiplicarString()


# # Problema 8

# In[4]:


def numeros(a,b,c):
    if a > 100 or b > 100 or c > 100:
        print(a+b+c)
    else:
        print(a*b*c)
    return

a = int(input())
b = int(input())
c = int(input())
numeros(a,b,c)


# # Problema 10

# In[22]:


def esPalindromo():
    palabra = input()
    if palabra[::-1] == palabra:
        print(True)
    else:
        print(False)
    return
esPalindromo()

