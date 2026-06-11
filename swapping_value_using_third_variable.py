# Getting value from user

num1 = int(input("Enter an integer value for num1 : "))
num2 = int(input("Enter an integer value for num2 : "))
temp = 0                                                        # initialize 0 into temp variable

print (f"Before swapping num1 = {num1} and num2 = {num2}")

temp = num1                                                     #store the value of num1 into temp so that num1 can store the value of num2 
num1 = num2                                                     #store the value of num2 into num1 
num2 = temp                                                     #store the value of temp into num2

print (f"After swapping num1 = {num1} and num2 = {num2}")
