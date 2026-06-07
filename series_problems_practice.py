########################
# 1 + 2 + 3 + . . . + n
########################

print("\n--------------------------")
print("1 + 2 + 3 + . . . + n = ?")
print("--------------------------")

n = int(input("Enter the last number :  "))
series1 = list(range(1, n + 1, 1))
total = 0
for x in series1:
    total = total + x
print (f"Sum of 1 to {n} is : {total}")

n = 0                                               # clear variable data to reuse
total = 0                                           # clear variable data to reuse
x =0                                                # clear variable data to reuse

########################
# 2 + 4 + 6 + . . . + n
########################

print("\n--------------------------")
print("2 + 4 + 6 + . . . + n = ?")
print("--------------------------")


n = int(input("Enter the last even number :  "))
series2 = list(range(2, n + 1, 2))
for x in series2:
    total = total + x
print (f"Sum of 2 to {n} is : {total}")

n = 0
total = 0
x =0

################################
# 1² + 3² + 5² + . . . + n² = ?
################################

print("\n--------------------------")
print("1² + 3² + 5² + . . . + n² = ?")
print("--------------------------")

n = int(input("Enter the last odd number :"))
series3 = list(range(1, n + 1, 2))
for x in series3:
    total = total + x*x
print (f"Sum of 1² to {n}² is : {total}")

