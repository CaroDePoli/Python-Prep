#!/usr/bin/env python
# coding: utf-8

# ## Flujos de Control

# 1) Crear una variable que contenga un elemento del conjunto de números enteros y luego imprimir por pantalla si es mayor o menor a cero

# In[4]:

a= 10
print(a)



# 2) Crear dos variables y un condicional que informe si son del mismo tipo de dato

# In[5]:

a= 5
b= '10'
if type(a) == type(b):
    print(f'Las variables {a} y {b} son del mismo tipo')
else:
    print('Las variables son distintas')



# 3) Para los valores enteros del 1 al 20, imprimir por pantalla si es par o impar

# In[7]:
for valores in range (1,21):
    if valores %2 == 0:
        print(f'El valor {valores} es un numero par')
    else:
        print(f'El valor {valores} es un numero impar')




# 4) En un ciclo for mostrar para los valores entre 0 y 5 el resultado de elevarlo a la potencia igual a 3

# In[9]:

for i in range(0,6):
    print('El numero ', str(i), 'elevado a la 3era potencia es igual a', str(i**3))



# 5) Crear una variable que contenga un número entero y realizar un ciclo for la misma cantidad de ciclos

# In[10]:
i=10
for i in range (0,11):
    pass
print(i)




# 6) Utilizar un ciclo while para realizar el factoreo de un número guardado en una variable, sólo si la variable contiene un número entero mayor a 0

# In[33]:

i= 5
if (type(i) == int):
    if(i  >0):
        factorial=i
        while(i > 2):
            i=i-1
            factorial= factorial * i
        print('el factorial es', factorial)
    else:
        print('la variable es menor a cero')
else:
    print('la variable no es un numero entero')
        

# 7) Crear un ciclo for dentro de un ciclo while

# In[38]:

contador=0
while contador < 5:
    print(f'este es el ciclo while nro. {contador}')
    print('*'*20)
    for i in range (0,5):
        print('este es el ciclo for nro', str(i))
    contador +=1


# 8) Crear un ciclo while dentro de un ciclo for

# In[3]:

n= 4
for i in range (1, n):
    while (n <4):
        n -=1
        print(f'este es el ciclo while {n}, dentro del ciclo for {i}')



# 9) Imprimir los números primos existentes entre 0 y 30

# In[54]:

for primo in range(1,31):
    for i in range(2, primo):
        if primo%i == 0:
            break
    else:
        print(primo)


# 10) ¿Se puede mejorar el proceso del punto 9? Utilizar las sentencias break y/ó continue para tal fin

# In[55]:

ciclos_con_break = 0
for primo in range (1,31):
    for numero in range (2,primo):
        ciclos_con_break +=1
        if primo %numero == 0:
            break
    else:
        print(primo, 'es un numero primo')
print('cantidad de ciclos con break', str(ciclos_con_break))



# 11) En los puntos 9 y 10, se diseño un código que encuentra números primos y además se lo optimizó. ¿Es posible saber en qué medida se optimizó?

# In[56]:


ciclos_sin_break = 0
tope_maximo= 30
n= 0
primo= True 
while (n< tope_maximo):
    for div in range (2, n):
        ciclos_sin_break += 1
        if (n% div == 0):
            primo= False
            
    if(primo):
        print(n)
    else:
        primo=True
    n+=1
print('cantidad de ciclos sin break ' +str(ciclos_sin_break))
print('se optimizó en ' + str((ciclos_con_break/ciclos_sin_break)*100) ,'%' )

# In[57]:




# 12) Aplicando continue, armar un ciclo while que solo imprima los valores divisibles por 12, dentro del rango de números de 100 a 300

# In[62]:

n=99
while (n<=300):
    n+=1
    if n%12 !=0:
        continue
    print('El numero', str(n), 'es divisible por 12')



# 13) Utilizar la función **input()** que permite hacer ingresos por teclado, para encontrar números primos y dar la opción al usario de buscar el siguiente

# In[73]:
n= 1
sigo = 1
primo = True
while(sigo == 1):
    for div in range (2 , n):
        if (n % div == 0):
            primo= False
            break
    if (primo):
        print(n)
        print('Quiere optener el siguiente numero primo?')
        if (input() != '1'):
            print ('El proceso finalizó')
            break
    else:
        primo= True
    n += 1



# 14) Crear un ciclo while que encuentre dentro del rango de 100 a 300 el primer número divisible por 3 y además múltiplo de 6

# In[75]:

n=100
while(n < 300):
    if (n %6 ==0):
        print('el numero ', str(n) ,'es divible por 3 y multiplo de 6')
        break
    n +=1


# %%
