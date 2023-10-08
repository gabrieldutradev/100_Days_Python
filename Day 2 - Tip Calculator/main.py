print("Welcome to the tip calculator.")
bill = float(input("What was the total bill? $"))
print(type(bill))
tip = int(input("What percentage tip would you like to give? 10%, 12%, or 15%? "))
print(type(tip))
people = int(input("How many people to split the bill? "))
print(type(people))

bill_with_tip = bill + (bill * (tip/100))
final_bill = bill_with_tip / people

bill_each_person = round(final_bill, 2)
print(bill_each_person)
#bill_each_person = "{:.2f}".format(final_bill)
#print(bill_each_person)
#bill_each_person = "{:.3f}".format(final_bill)
#print(bill_each_person)

print(f"Each person should pay: ${bill_each_person}")