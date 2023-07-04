import datetime
frase = "Olá Mundo, sou Sérgio Renato"
hoje = datetime.date.today()
hora = datetime.datetime.now()
print(frase)
print("Dia ", hoje)
print("Hora: ", hora.hour,":",hora.minute)
print("Minutos: " , hora.minute) 