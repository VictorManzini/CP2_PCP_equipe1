# Exercicio aula 03 - Peso do caminhão 
from time import sleep

print("""
------CALCULADORA DE CUSTO DOS CAMINHÕES------
      """)

print(""" Tabela:
     Estado  |   imposto                  Código da carga   |   Preço por Kg
        1    |   35%                           10 a 20      |    100.00
        2    |   25%                           21 a 30      |    250.00
        3    |   15%                           31 a 40      |    340.00
        4    |   5%
        5    |   ISENTO
""")
sleep(1)

def converter_peso(ton):
    peso_kg = ton * 1000
    return peso_kg

def calcular_preco(codigo_carga, peso_kg):
    if codigo_carga >= 10 and codigo_carga <= 20:
         preco_kg = 100
    elif codigo_carga > 20 and codigo_carga <= 30:
         preco_kg = 250
    elif codigo_carga > 30 and codigo_carga <= 40:
         preco_kg = 340
    else: 
        print("Código da carga inválido... Tente novamente")
        return 0
    preco_carga = preco_kg * peso_kg
    return preco_carga

def calcular_imposto(estado, preco_carga):
    if estado == 1:
         imposto = 0.35
    elif estado == 2: 
         imposto = 0.25
    elif estado == 3:
         imposto = 0.15
    elif estado == 4:
         imposto = 0.05
    else:
          imposto = 0
    valor_imposto = preco_carga * imposto
    return valor_imposto

def calcular_total(preco_carga, valor_imposto):
     return preco_carga + valor_imposto

ton = float(input("Digite o peso da carga (em toneladas): "))
estado = int(input("Digite o código do estado de origem da carga do caminhão (1 a 5): "))
codigo_carga = int(input("Digite o código da carga (10 a 40): "))

peso_kg = converter_peso(ton)
preco_carga = calcular_preco(codigo_carga, peso_kg)
valor_imposto = calcular_imposto(estado, preco_carga)
total = calcular_total(preco_carga, valor_imposto)

print(f"O peso da carga do caminhão é: {peso_kg:.2f}kgs ")
print(f"O preço da carga do caminhão é: R$ {preco_carga:.2f} ")
print(f"O valor do imposto cobrado em R$ é de: R$ {valor_imposto:.2f} ")
print(f"O valor total transportado (carga + impostos) é de: R$ {total:.2f} ")
