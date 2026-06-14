# Max and min number from user input number list
n = input("Enter integer numbers seperate with space : ")       # getting input from user as a string

n = n.split()               # split the user string
number = []                 # to store the user value as integer list

for x in n:
    number.append(int(x))   # store the splited string as integer list 

maxnumber = max(number)     # finding maxnumber using max() function
minnumber = min(number)     # finding minnumber using min() function

print ("maxnumber : ", maxnumber)
print ("minnumber : ", minnumber)
