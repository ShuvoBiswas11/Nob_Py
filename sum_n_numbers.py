#Getting User input

num = int(input("Enter the n-th number you want to sum : "))

#Initialize Variables

total = 0
i = 1

#Calculate the sum from 1 to num

while i <= num:
    total = total + i
    i = i + 1

#Display the result

print(f"The sum of numbers from 1 to {num} is : {total}")
