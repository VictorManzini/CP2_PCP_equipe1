def calcular_horas_extras(salario_base, horas):
    return salario_base * 0.015 * horas


def calcular_descontos_faltas(salario_base, faltas):
    return salario_base * 0.02 * faltas


def calcular_bonus(cargo, recebeu_bonus):
    if recebeu_bonus.lower() != "s":
        return 0

    cargo = cargo.lower()

    if cargo == "gerente":
        return 1000
    elif cargo == "analista":
        return 500
    elif cargo == "assistente":
        return 300
    elif cargo == "estagiario":
        return 100
    else:
        return 0


# Entrada de dados
nome = input("Digite seu nome: ")
cargo = input("Digite seu cargo (Gerente, Analista, Assistente, Estagiario): ")
salario_base = float(input("Digite o salário base: "))
horas_extras = int(input("Digite as horas extras trabalhadas: "))
faltas = int(input("Digite o número de faltas no mês: "))
recebeu_bonus = input("Recebeu bônus? (s/n): ")

# Cálculos
valor_horas_extras = calcular_horas_extras(salario_base, horas_extras)
descontos = calcular_descontos_faltas(salario_base, faltas)
bonus = calcular_bonus(cargo, recebeu_bonus)

salario_bruto = salario_base + valor_horas_extras + bonus
total_acrescimos = valor_horas_extras + bonus
total_descontos = descontos
salario_final = salario_bruto - total_descontos

# Saída
print("\n--- Resultado ---")
print(f"Funcionário: {nome}")
print(f"Salário bruto: R${salario_bruto:.2f}")
print(f"Total de acréscimos: R${total_acrescimos:.2f}")
print(f"Total de descontos: R${total_descontos:.2f}")
print(f"Salário final: R${salario_final:.2f}")