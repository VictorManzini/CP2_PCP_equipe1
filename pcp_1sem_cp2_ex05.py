# Aluno: Luiz Cesar Conti Salvador
#RM: 571305
def financiamento_aprovado(idade, renda, valor):
    return idade >= 18 and valor <= 20 * renda

def taxa_parcelas(parcelas):
    if parcelas < 3 or parcelas > 24:
        print("Parcela inválida, digite o valor desejado entre 3 e 24 parcelas.")
        exit()
    elif parcelas >= 3 and parcelas <= 6:
        return 0.05
    elif parcelas >= 7 and parcelas <= 12:
        return 0.08
    elif parcelas >= 13 and parcelas <= 24:
        return 0.10

def calcular_parcela(valor, taxa, parcelas):
    return valor * (taxa *(1 + taxa) ** parcelas) / ((1 + taxa) ** parcelas - 1)    

def valor_total(parcela, parcelas):
    return parcela * parcelas

def valor_juros(valor, valor_total):
    return valor_total - valor


nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade: "))
renda_mensal = float(input("Qual a sua renda mensal? "))
valor_desejado = float(input("Qual valor deseja pegar de empréstimo? "))
numero_parcelas = int(input("Qual número de parcelas deseja? (3 até 24) "))

if financiamento_aprovado(idade, renda_mensal, valor_desejado):

    taxa = taxa_parcelas(numero_parcelas)
    parcela = calcular_parcela(valor_desejado, taxa, numero_parcelas)
    total = valor_total(parcela, numero_parcelas)
    juros = valor_juros(valor_desejado, total)
    print("Financiamento aprovado")
    print(f"Cliente: {nome}")
    print(f"Valor financiado: R$ {valor_desejado:.2f}")
    print(f"Taxa de juros: {taxa * 100:.0f}% ao mês")
    print(f"Valor da parcela: {parcela:.2f}")
    print(f"Valor total pago: R$ {total:.2f}")
    print(f"Total de juros pagos: R$ {juros:.2f}")
else:
    print("Financiamento reprovado")
