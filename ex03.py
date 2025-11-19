#autor: davi elessandro
#data: 18/11/2025

seu_dinhiro = float(input("quanto de dinheiro você possui: "))
salgado = float(input("quanto custa o salgado? "))
suco = float(input("quanto custa o suco? "))

dinheiro_total_gasto = (salgado + suco)

troco = (seu_dinhiro - dinheiro_total_gasto)

print (f"seu troco e {troco}")