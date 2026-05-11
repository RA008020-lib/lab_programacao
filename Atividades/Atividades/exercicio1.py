vetor = []
for i in range (10):
    valor=int(input(f"Posição {i}: "))
    vetor.append(valor)
diferentes = 0
for i in range(10):
    encontrou = False
    for j in range(i):
        if vetor[1] == vetor[j]:
            encontrou = True
            break
    if not encontrou:
        diferentes += 1
print("Valores diferentes", diferentes)