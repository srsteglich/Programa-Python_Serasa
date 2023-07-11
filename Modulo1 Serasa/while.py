# pra comentario: seleciona e ctrl +;

#exemplo 1
conta = 10;
while conta >= 1:
   print (conta);
   conta -= 1;

# exemplo 2    
notas = [];
nota =  float(input("Digite uma nota (-1 para sair): "));
while nota >= 0 :
    notas.append(nota);
    nota = float(input("Digite uma nota (-1 para sair): "));
print(notas);

# exemplo 3
conta = 0;
senhaBloq = False;
senha = input("Informe a senha: ");
while senha != '123':
    print("Senha incorreta");
    conta += 1;
    if (conta == 3):
        senhaBloq = True;
        break;
    senha = input("Digite a senha: ")
if (senhaBloq)  :
    print("Sua Senha foi bloqueada, por 3 tentativas!!!\n");
else:    
    print("Senha correta!\n");

# exemplo 4
#numeros pares
quant = int(input("Informe a quantidade de numeros pares a serem impressos: "));
conta = 1;
while quant > 0:
    if conta % 2 == 0:
        # % 2 != 0 --> impares
        print(conta);
        quant -= 1;
    conta += 1;

# exemplo 5    
## jogo de adivinhacao
numSecreto = 20;
plapite = int(input("Digite um numero: "));

while plapite != numSecreto:
   print(" Voce errou...");
   plapite = int(input("Digite um numero: "));
print(" Parabens, voce acertou!!!! ");   

##exem 6 
palavra = input("Digite uma palavra ('sair' para encerrar)");
palavra = palavra.lower();
while palavra != 'sair':
    print(palavra);
    palavra = input("Digite uma palavra ('sair' para encerrar)");
    palavra = palavra.lower();
    
## Implementacao de munu
opcao = 0
while opcao != 4:
    print("Menu")
    print("1. Opcao 1")
    print("2. Opcao 2")
    print("3. Opcao 3")
    print("4. Sair")
    opcao = int(input("Informe a opcao seleciona:"))
    if opcao == 1:
        print("Opcao 1 Selecionada")
    elif opcao == 2:
        print("Opcao 2 Selecionada")
    elif opcao == 3:
        print("Opcao 3 Selecionada")
    elif opcao == 4:
        print("Sair...") 
        break  
    else:
        print("Opcao invalida....")             

## Emulando do While
secreta = "python"
counter = 0
while True:
    palavra = input("Informa palavra:").lower()
    counter += 1
    if secreta == palavra:
        print(" Voce acertou a palavra!")
        break
    #if (secreta != palavra and ):
    
    if (secreta != palavra and counter > 5):
        print(" Voce atingiu limite de tentativas!")
        break