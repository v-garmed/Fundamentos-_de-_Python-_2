import random 
## El modulo random permite generar números aleatorios 
# Generar 10 números aleatorios entre 0 y 1
for i in range (10):
    print(random.random())      #Esta funcion permite generar un número aleatorio entre 0 y 1 
print('final de seed aleatorio')
random.seed(0)  # Establece la semilla por lo que dejaran de ser numeros aleatorios

for i in range (10):
    print(random.random())      #Esta funcion permite generar un número aleatorio entre 0 y 1
print('final de seed 0')

#La funcion range tiene la siguiente estructura
# range(start, stop, step)

print(random.randrange(1, 10, 2))  # Genera un número aleatorio entre 1 y 10 con un paso de 2
print(random.randint(1, 10))  # Genera un número entero aleatorio entre 1 y 10 (incluidos)
print(random.randrange(1, 10))  # Genera un número entero aleatorio entre 1 y 10 (excluido)
print(random.randrange(1)) # Genera un número entero aleatorio entre 0 y 1 (excluido)
print('final de range') 
## Funcion choice

lista= [1,2,3,4,5,6,7,8,9,10]

print('inicio de choice y sample')
print(random.choice(lista))  # Elige un elemento aleatorio de la lista
print(random.sample(lista,3))  # Elige 3 elementos aleatorios de la lista sin repetición
print(random.sample(lista,2))  # Elige 3 elementos aleatorios de la lista con repetición
