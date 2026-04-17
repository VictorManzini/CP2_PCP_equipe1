# Arquivo do exercicio 3
# Aluno: Ricardo Tunes RM 555919
notas_sprints = []

nota_cps = []

nota_cp1 = float(input("Digite a primeira nota do CP: "))
nota_cps.append(nota_cp1)

nota_cp2 = float(input("Digite a segunda nota do CP: "))
nota_cps.append(nota_cp2)

nota_cp3 = float(input("Digite a terceira nota do CP: "))
nota_cps.append(nota_cp3)

nota_sprint_1 = float(input("Digite a primeira nota do Sprint: "))
notas_sprints.append(nota_sprint_1)

nota_sprint_2 = float(input("Digite a segunda nota do Sprint: "))
notas_sprints.append(nota_sprint_2)

nota_gs = float(input("Digite a nota da GS: "))


def menor_nota(notas):
    menor_nota = 10
    for nota in notas:
        if nota < menor_nota:
            menor_nota = nota

    print(f"A menor nota do CP e {menor_nota} e vai ser desconsiderada")
    return menor_nota


menor_nota_cp = menor_nota(nota_cps)

nota_cps.remove(menor_nota_cp)




print(nota_cps)

def calcular_media(nota_sprint, nota_cp, gs):

    media = 0

    for cp in nota_cp:
        media += cp

    for sprint in nota_sprint:
        media += sprint

    media = (media / 4) * 0.4 + gs * 0.6

    return media


media = calcular_media(notas_sprints, nota_cps, nota_gs)
media_com_peso = calcular_media(notas_sprints, nota_cps, nota_gs) * 0.4
print(f" A media do semestre sem peso e : {media}")
print(f" A media do semestre Anual (0.4) com peso e : {media_com_peso}")


