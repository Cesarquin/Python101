'''
def opera():
  num1 = int(input("Ingrese valor 1: "))
  num2 = int(input("Ingrese valor 2: "))
  return num1 + num2

print("El resultado de la suma es:", opera())
'''


# Función no retorna valor, no tiene parámetros:
def poten():
  base = int(input("Ingrese la base: "))
  expo = int(input("Ingrese el exponente: "))
  print("El resultado de elevar la base al exponente es:", base**expo)


poten()


#********************************
# Función no retorna valor, si tiene parámetros:
def poten2(B, E):
  print("El resultado de elevar la base al exponente es:", B**E)


base = int(input("Ingrese la base: "))
expo = int(input("Ingrese el exponente: "))
poten2(base, expo)
