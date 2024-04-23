a= 5
b= 7
if a<b:
    print('a es menor que b')
elif a>b:
    print('a es mayor que b')
elif a+b:
    print('es la suma de a + b')
else:
    print('a y b son iguales')
    
votos= 10001
if votos<10000:
    print('perdí las elecciones')
elif votos>10000:
    print('gané las elecciones')
else:
    print('voy a valotage')
breakpoint

edad= 16
if edad<15:
    print('aún te faltan cumplir años')
elif edad<60:
    print('ya los pasaste ja!')
elif edad > 60:
    print(' ya estas para jubilarte ja!')
else:
    print('ya tienes ', str(edad), ' eres quinceañera')

numeros=[0,2,4,6,8]
for num in numeros:
    suma= num+1
    print(suma)
    
for i in range(0,8):
    suma=i + 1
    print('variable de iteracion ',i, 'resultado= ', suma)
    
num=1
while num<10:
    print('numero', num)
    num= num+1