# Sum the digits of a number

number = input("Enter a number : ")         # get a number from user
total = 0

for x in number:                            # as the user input is a string it will iterate through the loop
    total = total + int(x)                  # to sum the digits each value should be converted into integer

print (f"Sum of all the digits of {number} is : {total}")
