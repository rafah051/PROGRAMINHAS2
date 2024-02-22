#Receber 3 notas

nota1 = float(input('Qual a nota do primeiro trimestre ?'))
nota2 = float(input('Qual a nota do segundo trimestre ?'))
nota3 = float(input('Qual a nota do terceiro trimestre ?'))

media = ((nota1 + nota2 + nota3)/3)

#Bloco de  decisões

if(media <4):
    print('Você é um burro')
    
elif(media <6):
    print('Reprovado')
    
else:
    print('Aprovado')