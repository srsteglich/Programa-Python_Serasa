"""
    Estrutura Condicionais  if, elif, else:
"""
"""
idade = int(input("Digite a sua idade: "));
if idade >= 18:
    print("Bem-vindo, você pode entrar na festa!!!");
else:
    print("Desculpe, você não pode entrar na festa!!!"); 
"""
    
"""  Numero 10 à 20 """
"""
num = 15;
if 10 <= num <= 20:
    print("O numero está dentro intervalo");
else:
    print("O numero está fora intervalo");
"""

"""   Comapara duas listas  """
"""
lista1 = [1,2,3];
lista2 = [1,2,3,4,5];
if len(lista1) > len(lista2):
    print(" A lista 1 é maior")
elif len(lista1) < len(lista2):
    print(" A lista 2 é maior")
else:
    print("A lista são iguais")
"""    
"""   Acesso um Sistema """
"""
senha = input("Digite sua senha: ");
senha_correta = 123;
if senha == senha_correta:
    print ("Usuario logado....");
else:
    print (" A senha está incorreta!!! ");
"""
#  Verficação de acesso um sistema com login e senha
usuario = input(" Digite o seu usuario: ");
senha = input(" Digite sua senha: ");

usuarioCorreto = 'admin';
senhaCorreto = 'admin';

if usuario != usuarioCorreto:
    print(" O usuario está incorreto!!!")
elif not senha == senhaCorreto:
    print(" A senha está incorreto!!!")        
elif usuario == usuarioCorreto and senhaCorreto == senhaCorreto:
    print (" Usuario e senha logado....");
else:
    print (" Usuario e senha está incorreta!!! ");
    
# Verificação de multiplas condições com and ou or

num = 10;
if (num > 0 and num <5) or (num > 10 and num <15):
    print (" O numero atende aos critérios");
else:
    print (" O numero não atende aos critérios");
    
# Verificação de uma condição negada
idade = 20;
possuiCarteira = False;

if idade >= 18 and not possuiCarteira:
    print(" Voce precisa de ter a carteira da motorista");
else:   
    print(" Voce está apto a dirigir")
    