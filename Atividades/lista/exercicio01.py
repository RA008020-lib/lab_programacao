import random

vetor1= []
vetor2 = [0,0,0,0,0,0]

for e in range (100):
    vetor1.append(random.randint(1,6))
for i in range (6):
    vetor2[i] = vetor1.count(i+1)

print(vetor1)
print(f"1: {vetor2[0]} | 2: {vetor2[1]} | 3: {vetor2[2]} | 4: {vetor2[3]} | 5: {vetor2[4]} | 6: {vetor2[5]} ")

import random

lancamentos=[]
for i in range(100):
    resultado=random.randint(1,6) 
    lancamentos.append(resultado)

frequencia = []
for face in range(1,7):
    quantidade = lancamentos.count(face)
    frequencia.append(quantidade) 
    
print("Vetor de frequências (quantidade de vezes das faces: 1, 2, 3, 4, 5, 6)")
print(frequencia)
print("\nvetor de lançamentos (100 vezes)")
print(lancamentos)