print(" ------  While e For  ------ ")
# print("Questao 1-")
# conta = 1;
# while conta <= 10:
#     print(conta);
#     conta += 1;
    
# print("\nQuestao 2-")
# for y in range(1,11):
#     print(y)   

# print("\nQuestao 3-")
# soma = 0;
# i = 1;
# while i <=100:
#     soma = soma + i;
#     i += 1;
# print(" A Soma dos números em While, de 1 à 100 é",soma);

# print("\nQuestao 4-")
# k = 100
# somar = 0
# for contas in range(1,k+1):
#     ##print(contas)
#     somar = somar + contas    
# print(" A Soma dos números em For, de 1 à 100 é",somar)    


# print("\nQuestao 5-")
# num = 1;
# while num <= 20:
#     if num % 2 == 0:
#         print(num);
#     num += 1;    

# print("\nQuestao 6-")
# for par in range(2,21,2):
#     print(par)
# print("\n Ou outro...\n")
# numpar = 1
# for p in range(1,21):
#     if numpar % 2 == 0:
#         print(numpar);
#     numpar += 1;

# print("\nQuestao 7-")
# letra =  str(input("Digite uma palavra: "))
# inver = ""
# quant = len(letra)-1
#  ##print("quant letra ",  quant)
# while quant >= 0: 
#      inver += letra[quant]
#      ##print(inver)
#      quant -= 1
# print(inver)

#       
#print("\nQuestao 9-")

print("\nQuestao 10-")
hobbies  = ["surf", "natação","programar","churrasco","musculação"]
for inverto in hobbies[::-1]:
    print(inverto)
print("\n Ou outro...\n ")
for inverto2 in reversed(hobbies):
    print(inverto2)
