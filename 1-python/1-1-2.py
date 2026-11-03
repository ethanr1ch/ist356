# Let' write a program to divide up the check among diners in a party.

# Write a program to input the amount of a restaurant check, tip %, and number of diners

# The program should output the total amount with tip, and the amount each diner owes.


bill = float(input("Enter the total amount of the bill $"))
if bill < 0:
	exit("Error: all values must be greater than or equal to 0.")

tip = int(input("What % would you like to tip, eg. 20 == 20%? "))
if tip < 0:
	exit("Error: all values must be greater than or equal to 0.")

diners = int(input("How many diners? "))
if diners < 0:
	exit("Error: all values must be greater than or equal to 0.")

total = bill + bill * tip / 100
share = total / diners

print("Total Bill, with Tip:", total)
print(f"Even share among {diners} diners is {share:.2f}")