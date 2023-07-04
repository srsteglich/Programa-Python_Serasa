listaNumeros = [7,2,8,4,5];
listaStrings = ['a','h','r','d'];
listaMistas = [1, "a", 3.14, True];
print(listaNumeros);
print(listaStrings);
print(listaMistas);

frutas = ["maça", "banana", "pera", "morango"];
print(frutas[1])
frutas[1]= "laranja";
frutas.append("Abacaxi");
print(frutas);
frutas.insert(1,"melancia");
print(frutas);
print(len(frutas))
print()
print ("Tamanho 2: ",len(frutas));
listaNova = [1,["a", "b"]];
print(listaNova[1][0]);

lista1 = [2,3,4];
lista2 = [8,2,7];
listaConcatada = lista1 + lista2;
print(listaConcatada);

listaRepete = [1] * 3;
print(listaRepete);

sublista = listaNumeros[1:4];
sublista2 = listaNumeros[1:2];
print("Seleciona numeros ",sublista);
print("Seleciona numeros2 ",sublista2);

print("numeros invertidos: ", listaNumeros[::-1])

frutaremover = frutas.remove("pera");
print(frutas);
print(frutaremover);
frutaremo2 = frutas.pop(2);
print(frutas);
print(frutaremo2);

frutas.sort();
print("Embaralhado: ", frutas);

print(frutas);




