con1 = {9, 8, 7, 6}
con2 = {'a', 'e', 'i', 'o', 'u'}
print(con1)
print(con2)
con3 = {1, 0, 3.4, True, 'abc', False}
print(con3)
con4 = {23, 54, 23, 9}
print(con4)
# función len():
print(len(con3))
# type()
print(type(con4))
# función set()
con5 = set('hola')
print(con5)
num1 = [23, 45, 56, 89]
con6 = set(num1)
print("Conjunto 6 =>", con6)
# Función add()
con6.add(99)
print(con6)
# Función update()
print("Conjunto 4 =>", con4)
con6.update(con4)
print(con6)
# Función remove()
con6.remove(99)
print(con6)
# Función discard()
con6.discard(100)
print(con6)
# Función clear()
con6.clear()
print(con6)
# OPERACIONES ENTRE CONJUNTOS:
# UNION
print("UNION DE CONJUNTOS:")
print("conjunto 1 =>", con1)
print("conjunto 4 =>", con4)
con2 = con1.union(con4)
print("unión =>", con2)
print("   |  =>", con1 | con4)
# INTERSECCIÓN
print("INTERSECCIÓN DE CONJUNTOS:")
con2 = con1.intersection(con4)
print("Intersección =>", con2)
print(" &    =>", con1 & con4)
# DIFERENCIA
print("DIFERENCIA:")
con2 = con1.difference(con4)
print(con2)
print(con1 - con4)
# DIFERENCIA SIMÉTRICA:
print("DIFERENCIA SIMÉTRICA")
con2 = con1.symmetric_difference(con4)
print(con2)
print(con1 ^ con4)
