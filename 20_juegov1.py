"""
Juego para adivinar un número aleatorio.
"""
import random

adivinar = random.randint(1, 100)
numero = 0
while numero != adivinar:
  numero = int(input('Sr usuario, digite un número: '))
  if (numero > adivinar):
    print('Digite un número menor')
  elif (numero < adivinar):
    print('Digite un número mayor')
  else:
    print("Acertaste!!!")

print("Fin del ciclo. ")
