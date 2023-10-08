# even = par
# odd = impar
# Modulo % > Verifica o resto da divisão. Se houver resto, é ímpar, se não houver, é par.
# 6 % 2 = 3 com resto 0

number = int(input("Digite um número: "))
if number % 2 == 0:
    print("Este é um número par.")
else:
    print("Este é um número ímpar.")