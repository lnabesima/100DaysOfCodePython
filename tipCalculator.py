print("Welcome to the Tip Calculator")
total_bill = float(input("What was the total bill? $"))

people_paying = int(input("How many people to split the bill? "))

tip_percentage_list = [10, 12, 15]
while True:
    tip_percentage = int(input(f"How much tip would you like to give? {tip_percentage_list} "))
    if tip_percentage in tip_percentage_list:
        break
    else:
        print("Please enter a valid tip percentage.")
        continue

total_bill_with_tip = total_bill * (1 + tip_percentage / 100)
total_for_each_person = round(total_bill_with_tip / people_paying, 2)
print(f"Each person should pay: ${total_for_each_person}.")
