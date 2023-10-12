states_of_america = ["Delaware", "Pennsylvania", "New York", "Texas", "Alaska", "Virginia", "Kansas"]

print(states_of_america[0])
print(states_of_america[3])
print(states_of_america[-1])
print(states_of_america[-4])
print(states_of_america[-2])

states_of_america[2] = "Pencilvania"

print(states_of_america[1])
print(states_of_america)

# adicionar ao final da lista append
states_of_america.append("Dixon")

print(states_of_america[-1])

# adicionar outra lista ao final da lista extend
states_of_america.extend(["Pipocaland", "Chuckland", "Branquelinholand"])
print(states_of_america)

