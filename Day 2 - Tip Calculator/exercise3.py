# 1st input: enter height in meters e.g: 1.65
height = input("Informe a altura: ")
# 2nd input: enter weight in kilograms e.g: 72
weight = input("\nInforme o peso: ")
# 🚨 Don't change the code above 👆

# Write your code below this line 👇
bmi = int(float(weight) / float(height)**2)
print(bmi)
print(type(bmi))
