#Initialize and Print Variable with List

subjects = ["VLSI", "RTL", "DFT", "PD", "DV", "SIGN OFF"]       #add string in list
num = [1, 2, 3, 4, 5, 6]                                        #add int in list
merge = ["VLSI", 1, "RTL", 2, "DFT", 3, "PD"]                   #add both string and int in list

print(f"Strings in List : {subjects}")
print(f"Int in List : {num}")
print(f"Both String And Int In List : {merge}")


#Print elements of merge in different way

print("\nPrint elements of merge in different way : ")
print(merge [2])                    #Print the 3rd element of list. merge = [0 1 2 3 4 5 6 . . .] 
print(merge [2:])                   #Print from 3rd element to last element of the list
print(merge [-1])                   #Print the last element of list
print("RTL" in merge)               #Check if 'RTL' is in merge
print(2 not in merge)               #Check if 2 is not in merge
print(num * 2)                      #Print the elements of num twice
print(num + ["verilog", "TCL"])     #Add elements in num without changing the real value of num

