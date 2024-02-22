#Recebendo a idade
idade= int (input('Qual a sua idade ?'))

#Bloco de decisões
if(idade < 13):
    print('Você é uma criança')

elif(idade < 18):
    print('Você é um adolecente')

elif(idade < 60):
    print('Você é um adulto')

else:
    print('Você é um idoso')