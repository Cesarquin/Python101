import math

print("Programa que permite realizar operaciones aritméticas entre dos números ingresados por el usuario"
)

while True:
  num1 = 0
  num2 = 0
  suma = 0
  resta = 0
  multiplicacion = 0
  division = 0
  op = 0

  print("Ingrese el primer número:")
  num1 = float(input())
  print("Ingrese el segundo número:")
  num2 = float(input())
  suma = num1 + num2
  resta = num1 - num2
  multiplicacion = num1 * num2
  division = num1 / num2

  print("Menú de opciones:")
  print("Digite 1 para sumar")
  print("Digite 2 para restar")
  print("Digite 3 para multiplicar")
  print("Digite 4 para dividir")
  op = int(input())

  if op == 1:
    print("El resultado de la suma es:", suma)
  elif op == 2:
    print("El resultado de la resta es:", resta)
  elif op == 3:
    print("El resultado de la multiplicación es:", multiplicacion)
  elif op == 4:
    print("El resultado de la división es:", division)

  print("¿Desea volver al menú anterior?")
  print("Digite 5 para volver al menú anterior")
  print("Digite 0 para salir del programa")
  op = int(input())

  if op == 5:
    continue
  else:
    break

#practica Octavio mostrando menu de opciones segun la operacion aritmetica que indique el usuario.
