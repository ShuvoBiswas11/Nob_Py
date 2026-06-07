#Printing every index of a list using while loop

#Initialize a list

print("Printing list elements using while loop : ")
number = list(range(10,101,10))         # number = 10 20 30 40 50 60 70 80 90 100

x = 0
while x < len(number) :                 # loop will run till x = 9
    print (number[x])
    x = x + 1


#Printing every index of a list using for loop

#Initialize a list

print("\nPrinting list elements using for loop : ")

number = list(range(10,101,10))

for y in number :                       # for loop will run for each value of number and store it in y
    print (y)
