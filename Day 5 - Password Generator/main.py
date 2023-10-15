#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91

# for let in range(1, nr_letters + 1):
letras_password = []
for let in range(1, nr_letters + 1):
    letra_aleatoria = random.choice(letters)
    letras_password.append(letra_aleatoria)
    #print(f"letra aleatória: {letra_aleatoria}")
password_letters = ''.join(letras_password)
#print(password_letters)

numbers_password = []
for num in range(1, nr_numbers + 1):
    numero_aleatorio = random.choice(numbers)
    numbers_password.append(numero_aleatorio)
    #print(f"numero aleatório: {numero_aleatorio}")
password_numbers = ''.join(numbers_password)
#print(password_numbers)

symbols_password = []
for sym in range(1, nr_symbols + 1):
    symbol_aleatoria = random.choice(symbols)
    symbols_password.append(symbol_aleatoria)
    #print(f"símbolo aleatório: {symbol_aleatoria}")
password_symbols = ''.join(symbols_password)
#print(password_symbols)

final_password = password_letters + password_numbers + password_symbols
#print(final_password)

#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P
lista_senha = list(final_password)
random.shuffle(lista_senha)
lista_senha_embaralhada = ''.join(lista_senha)
print(lista_senha_embaralhada)