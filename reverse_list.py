# Reverse a list

n = input("Enter a number of list : ")          # getting value from user as string

number = []                                     # to store the int value after splited the string value
reverse_list = []

n = n.split()                                   # split the user string

for x in n:
    number.append(int(x))                       # append the splited value as int in number variable

reverse_list = list(reversed(number))           # reverse the value of number using reversed() function

print(reverse_list)

