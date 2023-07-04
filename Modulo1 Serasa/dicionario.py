meuDicio = {
            "nome": "Sérgio", 
            "sobrenome": "Steglich" ,
            "idade": 44 
            #"nome": "Diego", 
            #"sobrenome": "Alves" ,
            #"idade": 33 , 
            #"nome": "Rick", 
            #"sobrenome": "Papo Furado" ,
            #"idade": 22 ,
            #"nome": "Marcos", 
            #"sobrenome": "Suda HiHIHI" ,
            #"idade": 25
            }
print(meuDicio)
print(" Valor do Dicio :", meuDicio['sobrenome'])

print()
meuDicio['Cidade'] = "Floripa" 
print(meuDicio)
meuDicio.pop('idade')
print(meuDicio)
print()
frutaDicio = {
    'maçã'   : 3,
    'banana' : 6,
    'uva'    : 8    
}
print()
print(frutaDicio)
print("Valor do Dicio ",frutaDicio['uva'])
frutaDicio['maçã']= 6
frutaDicio[' maçã']= 2
frutaDicio['Maçã']= 4
print(frutaDicio)
print("Quantidade: " ,frutaDicio.get("banana"))
print("Quantidade: " ,frutaDicio.get("abacaxi", "Não encontra fruta"))
frutaDicio.pop("uva")
print("Atualizar: ",frutaDicio)


animaisDicio = {}
animaisDicio["cachorro"] = "Mey"
print()
print(animaisDicio)

print()
aluno =  {
    'nome'    : 'Sergio',
    'idade'   : 22,
    'hobbies' : ['surfar', 'nadar', 'programar']
}
print(aluno)
print()

frutaDicio = {
    'maçã'   : 3,
    'banana' : 6,
    'uva'    : 8,
    'figo'   : 5 
}
print("Chaves: ",frutaDicio.keys())
print("Valores: ",frutaDicio.values())
print("Chaves e Valores: ",frutaDicio.items())
