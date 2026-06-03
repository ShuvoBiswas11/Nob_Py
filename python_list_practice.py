#Initialize and Print Variable with List

print("\n----Initialize and Print Variable with List----\n")
subjects = ["VLSI", "RTL", "DFT", "PD", "DV", "SIGN OFF"]       #add string in list
num = [1, 2, 3, 4, 5, 6]                                        #add int in list
merge = ["VLSI", 1, "RTL", 2, "DFT", 3, "PD"]                   #add both string and int in list

print(f"Strings in List : {subjects}")
print(f"Int in List : {num}")
print(f"Both String And Int In List : {merge}")


#Print elements of merge in different way

print("\nPrint elements of merge in different way : \n")
print(merge [2])                    #Print the 3rd element of list. merge = [0 1 2 3 4 5 6 . . .] 
print(merge [2:])                   #Print from 3rd element to last element of the list
print(merge [-1])                   #Print the last element of list
print("RTL" in merge)               #Check if 'RTL' is in merge
print(2 not in merge)               #Check if 2 is not in merge
print(num * 2)                      #Print the elements of num twice
print(num + ["verilog", "TCL"])     #Add elements in num without changing the real value of num


#Some functions of List

new_list = [1, 2, 3, 4]
print(f"\nNew List : {new_list}\n")
print("Length of the list : ")
print(len(new_list))                    #Print the length of the list [1 2 3 4 5 . .]

new_list.append("first")                #Add one element at the end of the list
print(new_list)

new_list.extend(["second", 5, 6])       #Add more than one elements at the end of the list
print(new_list)

new_list.insert(2, "Shuvo")             #Insert an element in a specific position [0 1 2 3 . .]
print(new_list)

new_list.remove("Shuvo")                #Remove an element from the list
new_list.remove("first")
new_list.remove("second")
print(new_list)

new_list.sort()                         #Sorting elements into ascending order
print(new_list)

new_list.reverse()                      #Sorting elements into descending order
print(new_list)

new_list.pop()                          #remove the last element of the list
print(new_list)

print(new_list.index(4))                #Print the index/position number of an element into a list

new_list.clear()                        #Clear all the elements of a list
print(new_list)











