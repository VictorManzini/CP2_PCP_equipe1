#recebe codigo de origem da carga (int 1 a 5), peso em tonelada, codigo da carga (int 10 a 40)
#calcula peso em quilos, preço da carga, valor do imposto com base no preço e no estado de origem, valor total (carga + impostos)

estado = int(input("Estado de origem (número inteiro, de 1 a 5): "))
peso = float(input("Peso da carga, em tonelada: "))
codigo = int(input("Código da carga (número inteiro, de 10 a 40): "))

if  10 <= codigo <= 20:
    preco_kg = 100
elif 21 < codigo <= 30:
    preco_kg = 250
elif 31 < codigo <=40:
    preco_kg = 340

if estado == 1:
    imposto = 35
elif estado == 2:
    imposto = 25
elif estado == 3:
    imposto = 15
elif estado == 4:
    imposto = 5
elif estado == 5:
    imposto = 0


peso_kg = peso * 1000
preco_carga = peso_kg * preco_kg
val_imp = preco_carga * (imposto / 100)
val_total = preco_carga + val_imp

print(f"Peso da carga: {peso_kg}kg")
print(f"Preço da carga: R${preco_carga}")
print(f"Valor do impostos: R${val_imp}")
print(f"Valor total (carga + impostos): R${val_total}")