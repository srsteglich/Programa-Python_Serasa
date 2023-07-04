tupla1 = (2,7,9)
tupla2 = ('g','s', 'TI', "Dev")
tupla3 = (1, 'Clipper', False)
tupla4 = 4,6,7,'Python'
print (tupla1)
print(tupla2)
print(tupla3)
print(tupla4)
print(type(tupla1))
print(type(tupla3))

# Acessando itens individual
print()
print(tupla3[1])
# Fatiar
print()
print(tupla1[1:4])

tupla5 = tupla2 + tupla3
print()
print("Concatenar ", tupla5)
a,b,c = tupla1
print("Valores das variaveis:" )
print(c)
print(b)
print(a)