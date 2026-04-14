# Exercicio da aula 03 - Ler três valores de um triângulo 
from time import sleep

print(""" 
------ TRIÂNGULOS ------
""")
sleep(0.7)

def triangulo(a, b, c):
    a, b, c = sorted([a, b, c], reverse = True)
    if a >= b + c: 
        return "NAO FORMA TRIANGULO"
    elif a == b == c:
        return "TRIANGULO EQUILATERO"
    elif a == b or b == c or c == a:
        return "TRIANGULO ISOSCELES"
    elif a**2 == b**2 + c**2:
        return "TRIANGULO RETANGULO"
    elif a**2 > b**2 + c**2:
        return "TRIANGULO OBTUSANGULO"
    elif a**2 < b**2 + c**2:
        return "TRIANGULO ACUTANGULO"  
    

a = float(input("Digite o lado A do triângulo: "))
b = float(input("Digite o lado B do triângulo: "))
c = float(input("Digite o lado C do triângulo: "))

print(f"O triângulo é: {triangulo(a, b, c)} ")
sleep(0.5)
print(f"Lado A = {a}")
sleep(0.5)
print(f"Lado B = {b}")
sleep(0.5)
print(f"Lado C = {c}")
sleep(0.7)
print("""

OBRIGADO POR USAR -TRIANGULOS-®
        ATÉ A PRÓXIMA!!!

""")