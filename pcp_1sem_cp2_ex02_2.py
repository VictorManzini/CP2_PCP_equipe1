#le 3 valores (lados de triangulo) e ordena em ordem crescente, sendo A o maior
#depois, determinar o tipo de triangulo

i = 0
A = float(input("Lado A: "))
B = float(input("Lado B: "))
C = float(input("Lado C: "))

if B > A:
    i = B
    B = A
    A = i
if C > A:
    i = C
    C = A
    A = i
if C > B:
    i = C
    C = B
    B = i

print(f"Lados em ordem decrescente: {A, B, C}\nEsses lados: ")

if A >= B + C:
    print("Não formam um triangulo")
elif A ** 2 == B ** 2 + C ** 2:
    print("Formam um triângulo retângulo")
elif A ** 2 > B ** 2 + C ** 2:
    print("Formam um triângulo obtusangulo")
elif A ** 2 < B ** 2 + C ** 2:
    print("Formam um triângulo actuangulo")
elif A == B or A == C or B == C:
    print("Formam um triângulo isoceles")
elif A == B == C:
    print("Formam um triângulo equilatero")