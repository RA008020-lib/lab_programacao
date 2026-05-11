import random

vetor = []
for i in range(50):
    vetor.append(random.randint(1,6))
    
contagem = 0
for i in range(50):
    if vetor[i] == 6:
        contagem += 1

percentual = (contagem / 50) * 100
print(f"Ocorrencias do 6: {contagem}")
print(f"Percentual: {percentual}%")