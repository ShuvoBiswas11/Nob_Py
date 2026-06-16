#Vowel and Consonant Count from User Input

n = input("Enter your text : ")         # taking input from user
vow = 0                                 # initiating variable to count vowel
cons = 0                                # initiating variable to count consonant

for x in n:
    x = x.lower()                       # convert user input in lower case
    
    if x >= "a" and x <= "z":           # condition to ignore spaces from user input
        
        if x in ("a", "e", "i", "o", "u"):
            vow = vow + 1
        else:
            cons = cons + 1

print ("vowel : ", vow)
print ("cons : ", cons)
