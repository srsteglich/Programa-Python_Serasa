fru = "banana"
hum = "é boa"
w = fru.replace("b", "z")
s = "s"
#t = len(fru)
frase = fru +' '+ hum
print(fru)
print(w)
print("quantidade da palavra:", len(fru+hum))
print(fru[1:5])
print("palavra invertida: ", fru[::-1])
print(fru.upper(),hum.upper())
print("quantos 'a':", fru.count('a',0,5))
print("quantos 'a':", hum.count('a',0,5))
print(fru.title()+s)
print(fru+s)
print()
nome = "Sérgio"
segundonome = "Renato"
sobrenome = "Steglich"
print(nome , segundonome +' '+ sobrenome)
print()
print("Acessando caracteres individuais: ")
print("Primeiro caracteres: ", fru[0])
print("Ultimo caracteres: ", fru[-1])
print (frase.split())



