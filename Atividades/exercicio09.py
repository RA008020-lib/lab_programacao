# Entrada de Dados 
porcentagem_agua = float(input("Qual a porcentagem da agua do reservatorio: "))
# Processamento
if porcentagem_agua >= 90:
    status = "CRÍTICO: Risco de transbordamento"
elif porcentagem_agua >= 50:
    status = "ADEQUADO: Fluxo adequado"
elif porcentagem_agua >= 20:
    status = "ATENÇÃO: Nível Baixo"
else:
    status = "PERIGO: Nível mínimo atingido"
print(f"O nível do reservatório está: {status} ")