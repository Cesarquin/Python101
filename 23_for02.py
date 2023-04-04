# Ciclo anidado:
f1 = [99, 88, 77]
f2 = [56, 45, 34]
f3 = [21, 43, 76]
matriz = [f1, f2, f3]
print(matriz)
# ciclo para visualizar los valores de la matriz:
for i in range(3):
  for j in range(3):
    print(matriz[i][j], end=' ')
  print()
# ciclo para ingresar los valores en matriz:
print('Ingreso de nuevos valores para la matriz:')
for i in range(3):
  for j in range(3):
    matriz[i][j] = float(input())
# ciclo para visualizar los valores de la matriz:
for i in range(3):
  for j in range(3):
    print(matriz[i][j], end=' ')
  print()


'''
for i in range(60):
  for j in range(60):
    print(i, " ", j)
'''