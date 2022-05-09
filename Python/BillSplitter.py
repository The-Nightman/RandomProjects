print("Welcome to the bill splitter and tip calculator")

bill = float(input("What was the total bill? £"))

tipPercent = int(input("What percentage tip would you like to give? 10, 12 or 15? "))

people = int(input("How many people to split the bill? "))

billPercent = bill / 100 * tipPercent

splitBill = round((bill + billPercent) / people, 2)

print(f"Each person should pay: £{splitBill}")
