n1 = 10;
n2 = 5;

soma  = n1 + n2;
subt  = n1 - n2;
mult  = n1 * n2;
divi  = n1 / n2;
resto = n1 % n2;
pote  = n1 ** n2;
print()
print(" ------   Operações Matematicos ------   ");
print("Soma: ", soma);
print("Subt: ", subt);
print("Mult: ", mult);
print("Divi: ", divi);
print("Resto: ", resto);
print("pote: ", pote);

numFloat = 3.14;
numArrendodar = round(numFloat);
print("Arrendodar: ",numArrendodar);
print();

import math
num = 4.7;
print("Valor Absoluto: ", abs(-4.7));
print("pra cima: ", math.ceil(num));
print("pra baixo: ", math.floor(num));

import random
print("Numero aleatorios de 1 a 1000:", random.randint(1,100));
print();
print("Numero aleatorios float de 0 a 1:", random.random());
print();

num3 = 123456789;
print(f"Numero 2 casas decimais {num3:.2f}");
print();
print("Numero 2 casas decimais {:.2f}".format(num3));
