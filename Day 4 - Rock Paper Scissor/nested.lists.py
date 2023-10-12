# Lista completa
# dirty_dozen = ["Strawberries", "Spinach", "Kale", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears", "Tomatoes", "Celery", "Potatoes"]

fruits = ["Strawberries", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears"]
vegetables = ["Spinach", "Kale", "Tomatoes", "Celery", "Potatoes"]

# 2 listas dentro de uma lista maior
dirty_dozen = [fruits, vegetables]
print(dirty_dozen)

# Funcionamento das nested lists
# O primeiro colchete se refere à lista, trazendo a lista inteira dessa forma

# Primeira lista
print(dirty_dozen[0])

# Segunda lista
print(dirty_dozen[1])

# Segunda lista
print(dirty_dozen[-1])

# O segundo colchete se refere ao index do item dentro da lista especificada no primeiro colchete
print(dirty_dozen[0][0])
print(dirty_dozen[1][3])

# Erro, neste caso não há lista 2
# print(dirty_dozen[2][1])