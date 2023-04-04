"""
Juego para adivinar un número aleatorio.
"""
import random
adivinar = random.randint(1, 100)
vidas = 5
numero = 0
while numero != adivinar and vidas > 0:
  vidas = vidas - 1  #vidas = 0
  numero = int(input('Sr usuario, digite un número: '))
  if numero > adivinar and vidas > 0:
    print('Digite un número menor')
  elif numero < adivinar and vidas > 0:
    print('Digite un número mayor')
  elif numero == adivinar:
    print("Acertaste!!!")

print("Fin del ciclo. ")
print(f"El valor a adivinar era {adivinar}")
