print("Thank you for choosing Python Pizza Deliveries!")
size = input("What size pizza do you want? S($15), M($20) or L($25? >")
add_pepperoni = input("Do you want pepperoni? Y or N. >")
extra_cheese = input("Do you want extra cheese? Y or N. >")
bill = 0

if size == "S":
    bill = 15
    print("Small size selected!")
elif size == "M":
    bill = 20
    print("Medium size selected!")
else:
    bill = 25
    print("Large size selected!")

#print("Add pepperoni for small pizza(Y or N): + $2")
if add_pepperoni == "Y":
    if size == "S":
        bill += 2
        print("Pepperoni added!")
    else:
        bill += 3
        print("Pepperoni added!")
else:
    print("Pepperoni didn't added!")

if extra_cheese == "Y":
    bill += 1
    print("Extra cheese added!")
else:
    print("Extra cheese didn't added!")

print(f"Your final bill is ${bill}.")