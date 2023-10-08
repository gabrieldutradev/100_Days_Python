3 + 5
7 - 4
3 * 2
a = 6 / 3 # Sempre retorna um float, a não ser que seja convertido
print(type(a))
print(type(int(a)))
print(int(a))
print(type(a))

print(2 ** 3)

# Prioridades
# ()
# **
# * /
# + -
print(3 * 3 + 3 / 3 - 3) # Resultado 7
print(3 * (3 + 3) / 3 - 3) # Resultado 3