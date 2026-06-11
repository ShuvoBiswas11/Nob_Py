# Getting value from user

num1 = int(input("Enter an integer value for num1 = "))
num2 = int(input("Enter an integer value for num2 = "))

print(f"Before swapping num1 = {num1} and num2 = {num2}")

num1 = num1 * num2      # assume num1 = 1, num2 = 2. here, num1 = 1 + 2 = 3
num2 = num1 / num2      # num2 = 3 - 2 = 1; which was the actual value of num1
num1 = num1 / num2      # num1 = 3 - 1 = 2; which was the actual value of num2

print(f"After swapping num1 = {int(num1)} and num2 = {int(num2)}")
