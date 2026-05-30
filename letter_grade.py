#Getting input from user


try:
    marks = int(input("Enter your marks : "))

#Condition


    if marks > 100 or marks < 0:
        print("Invalid Marks! Please enter marks between 0 and 100")

    elif marks >= 80:
        print("A+")

    elif marks >= 70:
        print("A")

    elif marks >= 60:
        print("A-")

    elif marks >= 50:
        print("B")

    elif marks >= 40:
        print("C")
    else:
        print("Fail")

except ValueError:
    print("Invalid Input! Please enter an integer.")
