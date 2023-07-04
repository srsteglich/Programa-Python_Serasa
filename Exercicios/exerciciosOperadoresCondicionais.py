
print(" ------  Estrutura de Dados  ------ ");
print("Questao 1-");
n1 = int(input(" Digite um número: "));
n2 = int(input(" Digite outro número: "));
soma  = n1 + n2;
subt  = n1 - n2;
mult  = n1 * n2;
divi  = n1 / n2;
print("\n ------   Operações Matematicos ------   ");
print("Soma         : ", soma);
print("Subttração   : ", subt);
print("Multiplicação: ", mult);
print("Divisão      :  {:.2f}".format(divi));

print("\nQuestao 2-");
cels = int(input(" Digite a temperatura da água: "));
if cels > 100:
   print("  A água está fervendo!!!");
   
print("\nQuestao 3-");   
num = int(input(" Digite um número: "));
if num % 2 != 0: 
    print( " É IMPAR");
else:
    print( " É PAR");  
    
print("\nQuestao 4-");   
#from getpass import getpass
#senha = getpass("Digite a senha: ");   
#print(senha)
senha = int(input(" Digite a senha: "))
if senha == 123456:
    print(" Senha com Sucesso, usuário logado... ")  

print("\nQuestao 5-");
idade = int(input(" Digite a sua idade: "));
if 18 <= idade <= 30:
    print(" A tua idade é",idade, "anos." );  
    
print("\nQuestao 6-");    
num1 = int(input(" Digite primeiro número: "));
num2 = int(input(" Digite segundo número: "));
num3 = int(input(" Digite terceiro número: "));
if num1 > 0:
    print(" Positivo. Núm:", num1);
elif num2 > 0:
    print(" Positivo. Núm:", num2);
elif num3 > 0:
    print(" Positivo. Núm:", num3);   
else:    
    print(" Os numeros digitados não são positivo");   
   
print("\nQuestao 7-");
letra = str(input("   Digite uma letra:"));
if letra in 'a,e,i,o,u,A,E,I,O,U':
    print(" É Vogal")
else:
    print(" É Consoante ou Outros")   
    
print("\nQuestao 8-");   
num8 = int(input(" Digite um número: "));
if num8 > 0:
    print(" É Positivo. Núm:", num8);
elif num8 < 0:
    print(" É Negativo. Núm:", num8);
elif num8 == 0:
    print(" É Zero:");      
       
print("\nQuestao 9-");
num91 = int(input("   Digite primeiro número: "));
num92 = int(input("   Digite segundo número: "));
num93 = int(input("   Digite terceiro número: "));

if (num91 < num92) and (num91 < num93) and (num92 < num93):
    print (" A ordem crescente: ", num91," - ", num92," - ",num93);
elif (num91 < num92) and (num91 < num93) and (num93 < num92):
    print (" A ordem crescente: ", num91," - ", num93," - ",num92); 
    
elif (num92 < num91) and (num92 < num93) and (num91 < num93):
    print (" A ordem crescente: ", num92," - ", num91," - ",num93); 
elif (num92 < num91) and (num92 < num93): #and (num93 < num91):    
    print (" A ordem crescente: ", num92," - ", num93," - ",num91);     
    
elif (num93 < num91) and (num93 < num92): #and (num91 < num92):
    print (" A ordem crescente: ", num93," - ", num91," - ",num92);
else: # não é necessario  (num93 < num92) and (num93 < num91) and (num92 < num91):  
    print (" A ordem crescente: ", num93," - ", num92," - ",num91);     
    
print("\nQuestao 10-");    
num10 = int(input("   Digite um número: "));
if num10 % 3 == 0 and num10 % 5 == 0:
    print(" É Multiplos de 3 e 5"); 
else:
    print(" NÃO É Multiplos de 3 e 5"); 
    
    
