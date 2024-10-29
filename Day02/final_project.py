# Initial Code
print("Welcome to the tip calculator")
total_bill = float(input("What was the total bill? $"))
tip = int(input("How much tip would you like to give? 10, 12, or 15? $"))
total_people = int(input("How many people to split the bill? "))


print(f"Each people should pay: ${round(((total_bill * (tip / 100)) + total_bill) / total_people, 2)}")

# Using more Variables to better understanding
print("Welcome to the tip calculator")
total_bill = float(input("What was the total bill? $"))
tip = int(input("How much tip would you like to give? 10, 12, or 15? $"))
total_people = int(input("How many people to split the bill? "))
total_bill_tip = total_bill * (tip / 100) + total_bill
final_total_individual = round(total_bill_tip / total_people, 2)

print(f"Each people should pay: ${final_total_individual}")