# Aluno: Luiz Cesar Conti Salvador
#RM: 571305
def financiamento_aprovado(idade, renda, valor):
    return idade >= 18 and valor <= 20 * renda

def taxa_parcelas(parcelas):
    if parcelas <= 6:
        return 0.05
    elif parcelas <= 12:
        return 0.08
    elif parcelas <= 24:
        return 0.10

def valor_parcela(valor, taxa, parcelas):
    if parcelas <= 6:
        return valor >= taxa * parcelas
    elif parcelas <= 12:
        return valor >= taxa * parcelas
    elif parcelas <= 24:
        return valor >= taxa * parcelas

def valor_total(parcela, parcelas):
    return parcela * parcelas

def valor_juros(valor, valor_total):
    return valor - valor_total


nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade: "))
renda_mensal = float(input("Qual a sua renda mensal? "))
valor_desejado = float(input("Qual valor deseja pegar de empréstimo? "))
numero_parcelas = int(input("Qual número de parcelas deseja? (3 até 24) "))

if idade >= 18 and valor_desejado <= 20 * renda_mensal:
    print("Financiamento aprovado")

    taxa = taxa_parcelas(numero_parcelas)
    parcela = valor_parcela(valor_desejado, taxa, numero_parcelas)
    total = valor_total(parcela, numero_parcelas)
    juros = valor_juros(valor_desejado, total)

    print("\n--- Financiamento aprovado ---")
    print(f"Cliente: {nome}")
    print(f"Valor financiado: R$ {valor_desejado:.2f}")
    print(f"Taxa de juros: {taxa * 100:.0f}% ao mês")
    print(f"Valor da parcela: {parcela:.2f}")
    print(f"Valor total pago: R$ {total:.2f}")
    print(f"Total de juros pagos: R$ {juros:.2f}")
else:
    print("Financiamento reprovado")
