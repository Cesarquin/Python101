'''
# ejercicio 1:
num = int(input())
print()
suma = 0
for i in range(num):
  valor = int(input())
  suma = suma + valor
print()
print(suma)
'''
'''
# ejercicio 2:
num = int(input())
print()
facto = 1
for i in range(1, num+1):
  facto = facto * i
print()
print(facto)
'''
'''
# ejercicio 3:
lista = []
print(lista)
num = int(input('Tamaño de lista: '))
print()
for x in range(num):
  A = int(input())
  lista.append(A)
print()
print(lista)
'''  
# ejercicio 4:
lista = input().split(" ")
print(lista)
'''
for i in range(len(lista)):
  lista[i] = int(lista[i])
'''
lista = list(map(int, lista))
print()
print(lista)

