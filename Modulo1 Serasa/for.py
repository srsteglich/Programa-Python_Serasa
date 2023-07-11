# exemplo 1 a 10
for num in range(1,11):
    print(num)
    
# 2      
frutas = ["maça", "pera", "uva"] 
for fruta in frutas:
    print(fruta)
    
# 2.1
for fruta in frutas:
    if fruta != "pera":
        print(fruta)
        
for fruta in frutas:
    if fruta == "pera":
        continue
    print(fruta)
      
# 2.2
for fruta in frutas:
    if (fruta == "pera"):
        print("Encontrou pera!")
        break
print(fruta)             

# 3  calculo da medias 
notas = [7.5, 8, 6.5, 9]
soma = 0
for nota in notas:
    soma += nota
media = soma / len(notas)
print("\n A média é: ", media)

# 4 conta vogais
palavra = "python"
vogais = 0
for letra in palavra:
    if letra in "aeiou":
        vogais += 1
print(f" A palavra {palavra} possui {vogais} vogal.\n")

# 5 itens de lista e alterar
lista = ["a", "b","c,","d"]
for indice in range(len(lista)):
    if indice == 0 :         
        print(f" O elemento no indice {indice} é {lista[indice]}")

# 6 incrementar um numero
print(" ")
for num in range(1,11,2):
    print(num)

# #7: inverter
palavra = "python"
for letra in reversed(palavra):
    print(letra)
  
#E 8: duas listas usando a zip()
lista1 = [1,2,3];
lista2 = ["a", "b", "c"]
for elemento1, elemento2 in zip(lista1, lista2):
    print(elemento1, elemento2)
  
# 9: acessar índice e elemento 
lista = ["a", "b", "c"]
for indice, elemento in enumerate(lista):
    print(f"O elemento no índice {indice} é {elemento}")   
for indice, elemento in enumerate(lista):
    if indice == 1:
        print("   " ,elemento)
 
# # 10: para acessar chaves e valores.
dicionario = {
    "chave1" : "valor1", 
    "chave2" : "valor2", 
    "chave3" : "valor3"
}
for chave, valor in dicionario.items():
    print(chave, valor)   
