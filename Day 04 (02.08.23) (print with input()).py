print("")
print("                 EB Department Information Collection Team")
print("")

name=input("Enter the House Owner Name: ")
number=int(input("Enter the Number of members in the house: "))
house_number=input("Enter the House Number: ")
units_used=float(input("Enter the electricity units used: "))
fans=float(input("Enter the electricity units used in fans: "))
lights=float(input("Enter the electricity units used in lights: "))
others=float(input("Enter the electricity units used in all others: "))
unit_amount=int(input("Enter the price amount of single unit: "))
total_unit_amount=unit_amount*units_used
gst_percent=int(input("Enter the percentage of gst for EB: "))
total_amount=total_unit_amount*(1+gst_percent)

print("")
print(f"{name} with {number} of his family members living on a house number {house_number} \nhave used electric units of fans as {fans} and lights as {lights} \nand on others as {others} generated an EB Bill of total of {units_used} units.")
print(f"With each unit as Rs.{unit_amount}, the total units sums up the electricity cost of \nRs.{total_unit_amount}. And in the addition of gst of {gst_percent}%, \nthe total amount on bill to be paid is {total_amount}")
print("")