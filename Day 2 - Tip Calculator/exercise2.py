

two_digit_number = input("Digite um número de 2 dígitos: ")
str(two_digit_number) # Converte em string
d1 = int(two_digit_number[0]) # Atribui a primeira letra da string em uma variável e converte em integer
d2 = int(two_digit_number[1]) # Atribui a segunda letra da string em uma variável e converte em integer
print("A soma das unidades é: " + str(d1 + d2))
