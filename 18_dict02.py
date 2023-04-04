estudiantes = {
  "Nombre": ["Cesar", "Augusto", "Mario"],
  "Código": [123, 456, 789],
  "Nota": [5, 3, 4]
}
print("estudiantes =")
print(estudiantes)
print("Valores del diccionario estudiantes =")
y = estudiantes.values()
print(y)
estudiantes["Nota"] = [4, 3, 4]
estudiantes['Materia'] = ["Quimica", "Biología", 'Matemáticas']
print(y)
print("Función items():")
print(estudiantes.items())
print("******** PARÉNTESIS *****")
lista1 = [1, 2, 3, 4]
print(1 in lista1)
tupla1 = (2, 3, 4)
print(5 in tupla1)
nombre = "Cesar Quintero"
print('a' in nombre)
print("****** FIN DE PARÉNTESIS *****" )
print('Nombres' in estudiantes)
print('Nombre' in estudiantes)
if 'Nombre' in estudiantes:
  print("Si, la llave nombre se encuentra en el dicccionario estudiantes")
print("Función update():")
print(f"estudiantes = {estudiantes}")
estudiantes.update({"Nombre": "Pedro"})
print(f"estudiantes = {estudiantes}")
estudiantes = {
  "Nombre": ["Cesar", "Augusto", "Mario"],
  "Código": [123, 456, 789],
  "Nota": [5, 3, 4]
}
print(f"estudiantes sin materia= {estudiantes}")
estudiantes.update(Materia = ['a', 'b'])
print(f"estudiantes.update(materia) = {estudiantes}")












