dic1 = {"Nombre": "Cesar", "Apellido": "Quintero", "Código": 1234}
dic2 = {"Nombre": "Carolina", "Apellido": "Gomez", "Código": 5432}
print(dic1)
print(dic2)
print(dic1['Nombre'])
print(dic2['Código'])
# Función len()
print(len(dic1))
# Función type()
print(type(dic1))
dic3 = dict(Nombre = "Cesar")
print(dic3)
# Indexing
x = dic1["Código"]
print(x)
print(f'dic1 = {dic1}')
# Función get()
print("get():")
print(dic1.get("Apellido"))
# Función keys()
print("keys(): ")
print(dic1.keys())
x = list(dic1.keys())
print(x)
# Adicionar llave:valor
print("Adicionar llave:valor")
dic1["Nota"] = 4
print(f'dic1 = {dic1}')
# Función values()
print(dic1.values())






