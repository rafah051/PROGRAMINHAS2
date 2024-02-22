#Conceito D: <= 3
#Conceito C: <= 6
#Conceito B: <= 8
#Conceito A: <= 10


#Receba a nota

nota = float (input('Digite aqui sua nota:'))

#Bloco de decisões

if(nota <= 3):
   print('Seu conceito é D e vocễ esta reprovado..')

elif(nota <= 6):
    print('Você esta na média, foi aprovado e está no conceito C')

elif(nota <= 8):
    print('Muito bem, você foi aprovado e está no conceito B')
    
else:
   print('Parabéns, você foi aprovado com sucesso e está no conceito A') 