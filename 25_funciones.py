# FUNCIONES:
# Retornan valor y no retornan valor
# FUNCION QUE NO RETORNA VALOR Y NO TIENE PARÁMETROS.
# Declaración de la función:
def imprimir():
  print("esta es una función,")
  print("que no retorna valor.")

# llamado a la función:
imprimir()
#
# FUNCION QUE NO RETORNA VALOR PERO SI TIENE PARÁMETROS.
# declaración de la fun:
def saludo(nombre='conocido'):
  print("Hola mi estimado", nombre)
# llamado a la fun con argumento sin retorno de valor.
saludo("Cesar")
saludo("viejo amigo")
saludo("Octavio")
saludo(123)
def imprilista(numeros):
  for num in numeros:
    print(num)
lista1 = [1, 3, 5, 8]
imprilista(lista1)
imprilista("Cesar")

