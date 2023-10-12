fruits = ['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana']

apple = fruits.count("apple")
print(apple)

tangerine = fruits.count("tangerine")
print(tangerine)

banana_index = fruits.index("banana")
print(banana_index)

# Próxima banana a partir da posição 4
print(fruits.index("banana", 4))
print(fruits.reverse)

fruits.append("grape")
print(fruits)

print("fruits.sort()")

# pop remove da lista e exibe, se não especificar pega o último item da lista
topo = fruits.pop()
print(topo)