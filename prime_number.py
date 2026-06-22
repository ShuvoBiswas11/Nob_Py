# Prime number checker

number = int(input("Enter any number : "))              # take a string from user and convert it into integer

if number <= 1:
    print(f"{number} is not a prime number")            # 1 and 0 are not prime number

else:
    for x in range(2,number):                           # if any divisors other than 1 and itself it will not a prime number
        if number % x == 0:
            print(f"{number} is not a prime number")
            break
    else:                                               # else statement must be ostside of the for loop
        print(f"{number} is a prime number")
