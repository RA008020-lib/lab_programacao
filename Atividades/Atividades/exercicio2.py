vetor = []
for i in range (5):
    valor=int(input(f"Posição {i}: "))
    vetor.append(valor)
x = int(input("Digite o valor de X: "))
posicao = -1
for i in range(5):
    if vetor [i] == x:
        posicao = i
        break

print(f"Posição: {posicao}")