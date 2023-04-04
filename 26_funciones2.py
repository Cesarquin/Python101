# FUNCIONES QUE RETORNAN VALOR Y NO TIENEN PARÁMETROS.
# declarando fun que retorna:
def suma():
  return 2 + 3
# llamando función que retorna:
A = suma()
print(suma())
print(A)
# FUNCIONES QUE RETORNAN VALOR Y SI TIENEN PARÁMETROS.
# declarando fun que retorna:
def resultado(A, B):
  return A + B
# llamando función que retorna:
print(resultado(2, 3))
print(resultado(3, 3))
print(resultado(54, 46))
print("Ejemplo de uso de funciones:")
num1 = int(input("Ingrese un valor: "))
num2 = int(input("Ingrese otro valor: "))
print("El resultado de la suma es:", resultado(num1, num2))


