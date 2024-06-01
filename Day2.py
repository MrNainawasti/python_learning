#bill_divider
print("Welcome to the bill divider.")
bill = int(input("What was the total bill? $"))
tip = int(input("How much (%)tip would you like to give? 10, 12 or 15?"))
people = int(input("How many people to split the bill?"))
total = round(bill + tip/100 * bill, 2)
per_person = round(total/people, 2)
print(f"Total amount to pay including tip: ${total}")
print(f"each person should pay:${per_person} ")

