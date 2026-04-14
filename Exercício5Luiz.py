nome=input("digite seu nome")
idade=int(input("Digite sua idade"))
renda_mensal=float(input("Qual a sua renda mensal?"))
valor_desejado=float(input("Qual valor deseja pegar de emprestimo?"))
numero_parcelas=input("Qual numero de parcelas deseja? 3 até 24 ")
valor_desejado_2=float(valor_desejado * 20)

if idade > 18 and valor_desejado_2 <= 20 * renda_mensal:
    print("Financiamento aprovado")
else:
    print("Financiamento reprovado")






