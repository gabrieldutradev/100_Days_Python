# names = names_string.split(", ")
# The code above converts the input into an array seperating
# each name in the input by a comma and space.

names = ["Angela", "Ben", "Jenny", "Michael", "Chloe"]
import random

# Coletar o numero 
num_itens = len(names)

# Transforma os nomes em números basicamente
random_choice = random.randint(0, num_itens - 1)

# Pega um nome aleatório da lista usando o numero aleatório
person_who_will_pay = names[random_choice]

print(person_who_will_pay + " is going to buy the meal today!")
