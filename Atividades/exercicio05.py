op = input("Deseja somar (S) ou multiplicar (M)? ")
if (op == "s" or op == "M"):
    x = float(input("Digite o primeiro número: "))
    y = float(input("Digite o segundo número: "))
    if (op == "S"):
        r= x + y 
        print("O resultado da soma:", r)
    elif (op == "M"):
        r= x * y
        print(f"O resultado da multiplicação: {r}")
    else:
        print("Opção inválida!")