target = int(input("Enter a number between 0 and 1000:\n")) # Enter a number between 0 and 1000
# Calcula a soma dos números pares 
sum_even = 0
for number in range(0 , target + 1):
  if number % 2 == 0:
    sum_even += number
print(sum_even)

# OU

even_sum = 0
for number in range(2, target + 1, 2):
  even_sum += number
print(even_sum)