print("1ª Questão ");
nome = input("Seu Nome: ");
idade = input("Tua idade: ");
print ("Olá, meu nome é" ,nome ,"e eu tenho",idade,"anos.");
print (f"Olá, meu nome é [nome] e eu tenho {idade} anos.");
print("2º Questão ");
frase = "Eu tenho 12 anos de expreincia em programação e ainda adoro trabalhar na area de programação.";
print (format(frase));
print("A quantidade da palavra:", len(frase));
print("3º Questão ");
sobrenome = "Steglich";
nomecompleto = nome +' '+ sobrenome;
print(nomecompleto);
print("4º Questão ");
print(frase.upper());
print("5º Questão ");
print (frase.split());
print("6º Questão ");
print (frase.replace("trabalhar","estudar"));
print("7º Questão ");
num1 = input("Escolhe um número: ");
num2 = input("Escolhe outro número: ");
soma = float(num1) + float(num2);
print ("A soma dos números: ",num1," + " ,num2," = ",soma);
print("8º Questão ");
num4 = input("Escolhe um número: ");
num5 = input("Escolhe outro número: ");
mult = float(num4) * float(num5);
print ("O produto dos números: ",num4," X " ,num5," = ",mult);
print();
