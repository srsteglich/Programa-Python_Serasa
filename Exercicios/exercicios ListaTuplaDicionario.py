print(" ------  LISTA  ------ ")
print("Questao 1-");
frutas = ["maça", "banana", "abacaxi", "melancia"];
print(" ", frutas);
print("Questao 2-");
frutas.append("uva");
print(" ", frutas);
print("Questao 3-");
frutas.remove("banana");
print(" ", frutas);
print("Questao 4-");
fruta_selecionada = frutas[1];
print(" ", fruta_selecionada);
print("")
print(" ------  TUPLA  ------ ")
print("Questao 5-");
cores = ("vermelho","azul","verde","amarelo","roxo");
print(" ", cores);
print("Questao 6-");
cor_selecionada = cores[2];
print(" ", cor_selecionada);
print("Questao 7-");
#cores.append("laranja");
print("  AttributeError: 'tuple' object has no attribute 'append'")
print("  Tradução: AttributeError: objeto 'tuple' não tem atributo 'append' ");
print("  Tuplas são imutáveis. Isso significa que não podemos inserir...");
print(" ", cores);
print("")
print(" ------  DICIONÁRIO  ------ ")
print("Questao 8-");
aluno = {
        "nome": "Sérgio",            
        "idade": 55, 
        "cidade" : "Floripa"
        }
print(" ", aluno);
print("Questao 9-");
aluno["idade_aluno"] = aluno["idade"];
aluno.pop('idade');
#print(" ",aluno)
print(" A idade do aluno: ", aluno["idade_aluno"], "anos.");
print("Questao 10-");
aluno['gênero'] = "Masculino";
print(" ",aluno);
print("Questao 11-");
aluno.pop("cidade");
print(" ",aluno);